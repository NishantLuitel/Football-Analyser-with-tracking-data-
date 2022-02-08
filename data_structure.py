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
        
        print('/nget method called/n')
        
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

            idxes = self.__find_columns(column_name)
          

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
                
        else:
            assert False, "Invalid argument type"
            
            
    def __find_columns(self,column_name):
        assert column_name in self.columns , "Invalid Column name"
        idxes = []
        for i in range(len(self.columns)):
            if column_name == self.columns[i]:
                idxes.append(i)
        return idxes
    
    
    def __display_dict(self,dic):
        max_length = len(max(list(dic.keys()),key = len))
        for elem in dic:
            print('{0:>{1}} : {2}'.format(elem,max_length,dic[elem]))
                               
        
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
            if str(column) in item2counts:
                item2counts[str(column)]+=1
            else:
                item2counts[str(column)] = 1
        item2counts_ordered = OrderedDict(sorted(item2counts.items(), key = lambda x:-x[1]))
        self.__display_dict(item2counts_ordered)
        

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
        
    
        
        



        
        