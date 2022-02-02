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
                for i in range(self.shape[0]):
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
            
            
            
        
        
    def __setitem__(self,column_name):
        pass
    
        
        
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
        
    
        
        



        
        