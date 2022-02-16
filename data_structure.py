 # -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 19:56:46 2022

@author: acer
"""
import csv
import os.path
from collections import OrderedDict


class dataFrame:
    
    
    def __init__(self,filename,skiprows = 0):
        
        self.__reader = None
        self.__rows = []
        
        if type(filename) == str: 
            assert os.path.isfile(filename) == True, "File not found"
            print("Reading...")
            self.__reader = csv.reader(open(filename))
            for row in self.__reader:
                self.__rows.append(row)
                #self.__rows = self.__rows[skiprows:]
            print("File read as custom dataFrame:",filename)
                
        elif type(filename) == list and type(filename[0]) == list:
            self.__rows = filename
            
        elif type(filename)==type(dataFrame([[''],['']])):
            column_names = filename.columns
            self.__rows = filename.__rows[skiprows+1:]
            self.__rows.insert(0,column_names)
            
            
    def __str__(self):
        
        max_index = len(super.__str__(self.shape[0]))
        InRange_row = min(5,self.num_rows)
        InRange_column = min(5,self.num_columns)
        
        
        #column header string
        string = '{0:>{1}}'.format('',max_index)
        for col_num in range(InRange_column):  
            item = str(self.columns[col_num])
            string+= '{0:>15.15}'.format(item)
        if self.num_columns > 4:
            string+= ' ... \n'
        else:
            string+='\n'
        
        #add other rows to the string
        for row_num in range(InRange_row):
            string += '{0:>{1}}'.format(row_num,max_index)
            for col_num in range(InRange_column):  
                item = str(self.__rows[row_num+1][col_num])
                string+= '{0:>15.15}'.format(item)
            if self.num_columns > 4:
                string+= ' ... \n'
            else:
                string+='\n'
            
        return string
    
    
    def __repr__(self):
        return self.__str__()
    

    def __getitem__(self,column_name):
        '''Implementing the bracket notation for accessing elements'''
        
        if type(column_name) == str:
         
            idxes = self.__find_columns(column_name)
            rows = []
            
            if self.shape[0] == 1 and len(idxes)==1:
                return self.__rows[1][idxes[0]]
#            elif len(idxes) ==1:                        ###############
#                return self.__rows[1:][idxes[0]]
            else: 
                for i in range(self.shape[0]+1):
                    column = []
                    for idx in idxes:
                        column.append(self.__rows[i][idx])
                    rows.append(column)
                return dataFrame(rows)
        
        elif type(column_name) == int:
            assert column_name>=0 and column_name<=self.num_rows-1 , "Index not in the range"
            rows = []
            if self.shape[1] == 1:
                return self.__rows[column_name+1][0]
            else:
                rows.append(self.columns)
                rows.append(self.__rows[column_name+1])
                return dataFrame(rows)
            
        elif type(column_name)==list:
            #returns dataframe from given list of indices            
            rows = []
            rows.append(self.columns)
            for column in column_name:
                if type(column) == int:
                    assert column>=0 and column<=self.num_rows-1 , "Index not in the range"
                    rows.append(self.__rows[column+1])
            return dataFrame(rows)  
                
            
        elif type(column_name) == tuple:
           column_name0 , column_name1 = column_name

           if type(column_name0) == str and type(column_name1) ==int:               
                assert column_name1>=0 and column_name1<=self.num_rows-1 , "Index not in the range"
                idxes = self.__find_columns(column_name0)
                i = idxes[0]
                print(idxes)
                return self.__rows[column_name1+1][i]
                
                
           elif type(column_name0) == int and type(column_name1) ==int:
                assert column_name0>=0 and column_name0<=self.num_rows-1 , "Index not in the range"
                assert column_name1>=0 and column_name1<=self.num_columns-1 , "Index not in the range"
                return self.__rows[column_name0+1][column_name1]
                
            
            
        else:
            assert False, "Invalid argument type"
            
        
    def __setitem__(self,column_name,item):
        '''Implementing the bracket notation for changing elements'''
               
        if type(column_name) == str:
            
            try:
                idxes = self.__find_columns(column_name)
            except AssertionError:
                #When no column is found new column is added with the given list item
                
                idx = len(self.columns)
                self.__rows[0].append(column_name)
                assert type(item) == list, "Item must be a list of values"
                if len(item)<=self.num_rows:
                    item_=['']*(self.num_rows - len(item))
                    item = item+item_
                    for i in range(self.num_rows):                        
                        self.__rows[i+1].append(item[i])
                    return
                else:
                    rows__ = [['']*(self.num_columns)]*(len(item)-self.num_rows)
                    self.__rows = self.__rows + rows__
                    for i in range(self.num_rows):                        
                        self.__rows[i+1].append(item[i])
                    return
                    
          
            # If some column_name is matched
            if type(item) == list and type(item[0]) == list:
                assert self.shape == (len(item),len(item[0])), "Argument shape mismatched"
                for i in range(self.shape[0]):
                    for n,idx in enumerate(idxes):
                        self.__rows[i+1][idx] = item[i][n]
                
            elif type(item) == type(dataFrame([[''],['']])):
                assert self.shape == item.shape, "Argument shape mismatched"
                for i in range(self.shape[0]):
                    for n,idx in enumerate(idxes):
                        self.__rows[i][idx] = item.__rows[i][n]
                
            elif len(idxes)==1 and type(item) == list:
                item_lists = []
                for el in item:
                    item_lists.append([el])
                assert self.shape[0] == len(item_lists) , "Item should either be a list or 2d-list"
                for i in range(self.shape[0]):
                    for idx in idxes:
                        self.__rows[i+1][idx] = item_lists[i][0]                                
            
            
            elif type(item) != list:
                assert self.shape[0] == 1, "Assignment cannnot be made"
                idxes = self.__find_columns(column_name)
                self.__rows[1][idxes[0]] = item
                
                
        
        elif type(column_name) == int:
            assert column_name>=0 and column_name<=self.num_rows-1 , "Index not in the range"

            if type(item) == list and type(item[0]) == list:
                assert self.shape == (len(item),len(item[0])), "Argument shape mismatched"
                self.__rows[column_name+1] = item[column_name]
                
            elif type(item) == type(dataFrame([[''],['']])):
                assert self.shape == item.shape, "Argument shape mismatched"
                if self.columns == item.columns:
                    self.__rows[column_name+1] = item.__rows[column_name+1]
                
            elif self.shape[1] == 1 and type(item) == list:
                item_lists = []
                for el in item:
                    item_lists.append(list(el))
                assert self.shape[0] == len(item_lists) , "Item should either be a list or 2d-list"
                self.__getitem__(column_name).__rows[1:] = item_lists
                
            elif type(item) == list:
                assert self.shape[1] == len(item) ,"Item should be a list"
                self.__rows[column_name+1] = item
                
            
            elif type(item) != list:
                assert self.shape[1] != 1, "Assignment cannnot be made this way"  
                self.__rows[column_name+1][0] = item


        elif type(column_name) == tuple:
            column_name0 , column_name1 = column_name
            if type(column_name0) == str and type(column_name1) ==int and type(item) != list:
                assert column_name1>=0 and column_name1<=self.num_rows-1 , "Index not in the range"
                idxes = self.__find_columns(column_name0)
                self.__rows[column_name1+1][idxes[0]] = item
                

            elif type(column_name0) == int and type(column_name1) ==int and type(item) != list:
                assert column_name0>=0 and column_name0<=self.num_rows-1 , "Index not in the range"
                assert column_name1>=0 and column_name1<=self.num_columns-1 , "Index not in the range"
                self.__rows[column_name0+1][column_name1] = item
         
        #column name is treated as index
        elif type(column_name) == list:
            assert self.shape[1] == 1,"Cannot call - on more than one column"
            if type(item) == list:
                assert len(column_name) == len(item), "length of index should match length of input list"
                for i,j in enumerate(column_name):
                    self.__rows[j+1] = [item[i]]
            elif type(item) == str or type(float(item)) == float:
                for i in column_name:
                    self.__rows[i+1][0] = item
            else:
                assert False, "Item should be either be list or primitive data "
            
            
        else:
            assert False, "Invalid argument type"
            
    def __eq__(self,item):
        '''Implementing '==' for dataFrame '''
        
        # When the equality check is done with a dataFrame object
        if type(item)==type(dataFrame([[''],['']])):
            if self.shape == item.shape:
                return self.__rows == item.__rows
            else:
                return False
            
        # When the equality check is done with a item present in the column dataFrame 
        else:
            assert self.shape[1] == 1 , "Cannot check equality on more than one column"
            indexes = [i for i,element in enumerate(self.aslist) if element == item]
            
            #Returns False if no item is matched or list of index if some items are matched
            if len(indexes) == 0:
                return False
            else:
                return indexes
    def __gt__(self,item):
        '''Implementing '==' for dataFrame '''
        
        # When the equality check is done with a dataFrame object
        #if type(item)==type(dataFrame([[''],['']])):
        #    if self.shape == item.shape:
        #        return self.__rows == item.__rows
        #    else:
        #        return False
            
        # When the equality check is done with a item present in the column dataFrame
        if False:
            pass
        else:
            assert self.shape[1] == 1 , "Cannot check equality on more than one column"
            indexes = [i for i,element in enumerate(self.aslist) if float(element) > float(item)]
            
            #Returns False if no item is matched or list of index if some items are matched
            if len(indexes) == 0:
                return False
            else:
                return indexes
            
            
    def __lt__(self,item):
        '''Implementing '==' for dataFrame '''
        
        # When the equality check is done with a dataFrame object
        #if type(item)==type(dataFrame([[''],['']])):
        #    if self.shape == item.shape:
        #        return self.__rows == item.__rows
        #    else:
        #        return False
            
        # When the equality check is done with a item present in the column dataFrame 
        

        if False:
            pass
        else:            
            if self.__isfloat(item):
                assert self.shape[1] == 1 , "Cannot check less than on more than one column"
                indexes = [i for i,element in enumerate(self.aslist) if float(element) < float(item)]
                
                #Returns False if no item is matched or list of index if some items are matched
                if len(indexes) == 0:
                    return False
                else:
                    return indexes
            else:
                assert False, "item should be convertible datatype or a dataFrame of same shape "
            
    def __ne__(self,item):
        '''Implementing '!=' for dataFrame '''
        
        
        value = (self == item)
        
        if type(value) == bool:
            return (not value)
        elif type(value)==list:
            indexes = [i for i in range(self.num_rows) if i not in value]
            return indexes
            
    def __truediv__(self, item):
        '''Implementing '/' operator for dataFrame'''
        
        assert self.shape[1] == 1,"Cannot call / on more than one column"
        truediv_array = [['']]*self.num_rows
        
        #Simple broadcasting
        if  self.__isfloat(item):
            for i in range(self.num_rows):
                truediv_array[i] = [round(float(self[i])/float(item),4)] if self.__isfloat(self[i]) else [float('NaN')]
            truediv_array.insert(0,[self.columns[0]])
            return dataFrame(truediv_array)
        
        #When item is a dataFrame
        #Note that column name of the returned dataframe is the column name of first operand
        elif type(item) == type(dataFrame([[''],['']])):
            assert self.shape == item.shape , "No of rows mismatched"
            for i in range(self.num_rows):
                truediv_array[i] = [round(float(self[i])/float(item[i]),4)] if (self.__isfloat(self[i]) and self.__isfloat(item[i])) else [float('NaN')]
            truediv_array.insert(0,[self.columns[0]])
            return dataFrame(truediv_array)
        
        else:
            assert False,"item should be float convertible datatype or a dataFrame of same shape"
            
                
    def __add__(self, item):
        '''Implementing '+' operator for dataFrame'''
        
        assert self.shape[1] == 1,"Cannot call + on more than one column"
        add_array = [['']]*self.num_rows
        
        #Simple broadcasting
        if  self.__isfloat(item):
            for i in range(self.num_rows):
                add_array[i] = [round(float(self[i])+float(item),4)] if self.__isfloat(self[i]) else [float('NaN')]
            add_array.insert(0,[self.columns[0]])
            return dataFrame(add_array)
        
        #When item is a dataFrame
        elif type(item) == type(dataFrame([[''],['']])):
            assert self.shape == item.shape , "No of rows mismatched"
            for i in range(self.num_rows):
                add_array[i] = [round(float(self[i])+float(item[i]),4)] if (self.__isfloat(self[i]) and self.__isfloat(item[i])) else [float('NaN')]
            add_array.insert(0,[self.columns[0]])
            return dataFrame(add_array)
            
        else:
            assert False,"item should be convertible datatype or a dataFrame of same shape"
                
    def __sub__(self, item):
        '''Implementing '-' operator for dataFrame'''
        
        assert self.shape[1] == 1,"Cannot call - on more than one column"
        sub_array = [['']]*self.num_rows
        
        #Simple broadcasting
        if  self.__isfloat(item):
            for i in range(self.num_rows):
                sub_array[i] = [round(float(self[i])-float(item),4)] if self.__isfloat(self[i]) else [float('NaN')]
            sub_array.insert(0,[self.columns[0]])
            return dataFrame(sub_array)
        
        #When item is a dataFrame
        #Note that column name of the returned dataframe is the column name of first operand
        elif type(item) == type(dataFrame([[''],['']])):
            assert self.shape == item.shape , "No of rows mismatched"
            for i in range(self.num_rows):
                sub_array[i] = [round(float(self[i])-float(item[i]),4)] if (self.__isfloat(self[i]) and self.__isfloat(item[i])) else [float('NaN')]
            sub_array.insert(0,[self.columns[0]])
            return dataFrame(sub_array)
        

        
        else:
            assert False,"item should be float convertible datatype or a dataFrame of same shape"
                
    def __pow__(self, item):
        '''Implementing '**' operator for dataFrame'''
        
        assert self.shape[1] == 1,"Cannot call - on more than one column"
        pow_array = [['']]*self.num_rows
        
        #Simple broadcasting
        if  self.__isfloat(item):
            for i in range(self.num_rows):
                pow_array[i] = [round(float(self[i])**float(item),4)] if self.__isfloat(self[i]) else [float('NaN')]
            pow_array.insert(0,[self.columns[0]])
            return dataFrame(pow_array)
        
        #When item is a dataFrame
        #Note that column name of the returned dataframe is the column name of first operand
        elif type(item) == type(dataFrame([[''],['']])):
            assert self.shape == item.shape , "No of rows mismatched"
            for i in range(self.num_rows):
                pow_array[i] = [round(float(self[i])**float(item[i]),4)] if (self.__isfloat(self[i]) and self.__isfloat(item[i])) else [float('NaN')]
            pow_array.insert(0,[self.columns[0]])
            return dataFrame(pow_array)
        

        
        else:
            assert False,"item should be float convertible datatype or a dataFrame of same shape"
            
            
            
    def __find_columns(self,column_name):
        '''returns the list of all indexes for the given column name present in the dataFrame'''
        
        assert column_name in self.columns , "Invalid Column name"
        idxes = []
        for i in range(len(self.columns)):
            if column_name == self.columns[i]:
                idxes.append(i)
        return idxes
    
    
    def __display_dict(self,dic):
        max_length = len(max(list(dic.keys()),key = len))
        for elem in dic:
            print('{0:<{1}} : {2}'.format(elem,max_length,dic[elem]))
        print('\n')        
    
    
    def __isfloat(self,x):
        try:
            float(x)
            return True
        except ValueError:
            return False
        except TypeError:
            return False
        
    #Bi-type
    def __find_first_index_ofTwo(self,value):
        '''Uses bisection search algorithm to find the index
        
            NOTE: Only works if type and non-type elements are present
            where the given value is type and all others are non type
            and type elements always occur together at last'''
        
        assert self.shape[1] == 1,"Cannot find index on more than one column with this method"
        low = 0 
        lst = self.aslist
        high = len(lst)-1
        idx = -1
        
        #Bisection implementation
        while low <= high:
            mid = (high+low)//2
            
            if self[mid] == value:
                idx = mid
                high = mid-1
            
            elif self[mid] != value:
                low = mid+1
                
            
        if idx != -1:
            return idx
        else:
            assert False, "Element Not Found"

    
        
    def change_columnName(self,name):
        if isinstance(name,list):
            assert self.num_columns == len(name) , "Number of columns mismatched"
            self.__rows[0] = name
        else:
            assert False, "Argument for column should be given as a list"
                      
            
    def value_counts(self):
        assert self.shape[1] == 1,"Cannot call value_counts on more than one column"
        column_items = self.aslist
        
        item2counts = {}
        for column in column_items:
            if column == '' or column == 'NaN':
                continue
            if str(column) in item2counts:
                item2counts[str(column)]+=1
            else:
                item2counts[str(column)] = 1
        item2counts_ordered = OrderedDict(sorted(item2counts.items(), key = lambda x:-x[1]))
        self.__display_dict(item2counts_ordered)
        
    def diff(self):
        assert self.shape[1] == 1,"Cannot call value_counts on more than one column"
        
        diff_array = [['']]*self.num_rows
        for i in range(self.num_rows):
            if (i-1 >=0) and self.__isfloat(self.__getitem__(i)) and self.__isfloat(self.__getitem__(i-1)):
                diff_array[i] = [round(float(self.__getitem__(i))-float(self.__getitem__(i-1)),4)]
            else:
                diff_array[i] = ['NaN']
        diff_array.insert(0,[self.columns[0]])
        return dataFrame(diff_array)
    
  
        
    def find_firstOfTwo(self, value):
        '''Finds the first index of given value'''
        
        return self.__find_first_index_ofTwo(value=value)
        
    def find_last_validOfTwo(self):
        '''Only 'NaN' are counted as Invalid
            It returns -1 if no valid element is present
            
            NOTE: Only works if invalid item is present after all the valid items and are all together
            '''
        
        return self.__find_first_index_ofTwo('NaN') - 1
    
    def find_lastOfTwo(self):
        ''' ('') is considered as last element in columns'''
        
        return self.__find_first_index_ofTwo('') - 1

    @property
    def aslist(self):
        '''Returns python-list rather than dataFrame'''
        if self.shape[0] == 1:
            return self.__rows[1]
        elif self.shape[1] == 1:
            return [x[0] for x in self.__rows[1:]]
        else:
            return self.__rows[1:]
        
    @property    
    def columns(self):
        return self.__rows[0]
    
    @property
    def num_columns(self):
        return len(self.columns)
    
    @property
    def num_rows(self):
        return len(self.__rows)-1
    
    @property
    def shape(self):
        '''Returns the shape of dataFrame'''
        return (len(self.__rows)-1,len(self.columns))
    
    @staticmethod
    def save_as_csv(x,filename):
        '''Save the file as csv'''
        assert type(x)==type(dataFrame([[''],['']])) and type(filename) == str , "Arguments type mismatched"
        assert filename.endswith('.csv'), "File is not in .csv format"
        x.__filename = filename
        with open(filename, "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(x.__rows)
        
    
        
        



        
        