# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:51:43 2022

@author: acer
"""

#   Learn to analyze tracking data


data_structure.py consists of a mannually built dataframe class and is suppossed to work like pandas dataFrame object 


Use m[row_number] returns dataframe with correspoing row as a reference
Use m[column_name] returns dataframe with correspoing column but by 

m[row_number][column_name] is writable
m[column_name][row_number] isn't writable




This project can be slightly modified to animate pitch control for any event



    #   Y                                                  Y
    #   |                                                  | 
    #   |                                                  |
    #   |(0,0)                        (1,0)                |(-0.5,0.5)                    (0.5,0.5)
    #   ,--------------,--------------,                    ,--------------,--------------,
    #   |              |              |                    |              |              |
    #   |--,           |           ,--|                    |--,           |           ,--|
    #   |  |          <|>(0.5,0.5) |  |         ------>    |  |          <|>(0,0)     |  |
    #   |--'           |           '--|                    |--'           |           '--| 
    #   |              |              |                    |              |              |  
    #   '--------------'--------------'  ------X           '--------------'--------------'------X
    #   (0,1)                         (1,1)                (-0.5,-0.5)                         (0.5,-0.5)
    #
    #    Metrica sports coordinate                                Our metric system
    #    --------------------------                               ----------------------               