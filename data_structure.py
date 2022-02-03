 # -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 19:56:46 2022

@author: acer
"""
import csv
import os.path


class dataFrame:
    
    
    def __init__(self,filename= None):
        
        self.__reader = None
        self.__rows = []
        
        if type(filename) == str: 
            if os.path.isfile(filename):
                print("Reading...")
                self.__reader = csv.reader(open(filename))
                for row in self.__reader:
                    self.__rows.append(row)
                print("File read as custom dataFrame:",filename)
        else:
            self.__rows = filename
            

        
    def __str__(self):
        #return ("{0}".format(len(self.__rows)-1))
        
        max_index = len(super.__str__(self.shape[0]))
        InRange_row = min(4,self.num_rows)
        InRange_column = min(3,self.num_columns)
        
        
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
            assert column_name in self.columns , "Column name is incorrect"
            idxes = []
            rows = []
            for i in range(len(self.columns)):
                if column_name == self.columns[i]:
                    idxes.append(i)
            
            if self.shape[0] == 1 and len(idxes)==1:
                return self.__rows[1][idxes[0]]
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
        
        else:
            assert False, "Invalid argument type"
            
        
            
    def __setitem__(self,column_name,item):
        '''Implementing the bracket notation for changing elements'''
        

        
        if type(column_name) == str:
            assert column_name in self.columns , "Column name is incorrect"
            idxes = []
            for i in range(len(self.columns)):
                if column_name == self.columns[i]:
                    idxes.append(i)            

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
                assert self.shape[0] == 1 and self.shape[1] == 1, "Assignment cannnot be made"
                self.__rows[1][0] = item
                
                
        
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
                assert self.shape[0] == 1 and self.shape[1] == 1, "Assignment cannnot be made"
                self.__rows[1][0] = item

        else:
            assert False, "Invalid argument type"
        

        
            
            
        
        
    #def __setitem__(self,column_name):
    #    pass
    
        
        
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
        
    
        
        



        
        