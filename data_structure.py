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
        
        
        #column header string
        string = '{0:>{1}}'.format('',max_index)
        for col_num in range(3):  
            item = self.columns[col_num]
            string+= '{0:>15.15}'.format(item)
        string+= ' ... \n'
        
        #add other rows
        for row_num in range(4):
            string += '{0:>{1}}'.format(row_num,max_index)
            for col_num in range(3):  
                item = self.__rows[row_num+1][col_num]
                string+= '{0:>15.15}'.format(item)
            string+= ' ... \n'
            
        

        
        
        return string
    
    def __repr__(self):
        return 
    
        
    
    
    def __getitem__(self,column_name):
        
        if type(column_name) == str:
            assert column_name in self.columns , "column name is incorrect"
            
            idxes = []
            rows = []
            for i in range(len(self.columns)):
                if column_name == self.columns[i]:
                    idxes.append(i)
            for i in range(self.shape[0]):
                column = []
                for idx in idxes:
                    column.append(self.__rows[i][idx])
                rows.append(column)
            return dataFrame(rows)
        
        
                    
        
    
    
    
    @property    
    def columns(self):
        return self.__rows[0]
    
    @property
    def num_columns(self):
        return len(self.columns)
    
    @property
    def shape(self):
        '''Returns the shape of dataFrame'''
        return (len(self.__rows),len(self.columns))
    
    
    
        
        



        
        