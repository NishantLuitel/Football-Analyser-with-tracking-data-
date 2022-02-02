# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 22:06:30 2022

@author: acer
"""

import data_structure
#import pandas as pd


filename = 'data/Sample_Game_2/Sample_Game_2_RawEventsData.csv'
filename_away_track = 'data/Sample_Game_2/Sample_Game_2_RawTrackingData_Away_Team.csv'
filename_home_track = 'data/Sample_Game_2/Sample_Game_2_RawTrackingData_HOme_Team.csv'




x = data_structure.dataFrame(filename)
#y = pd.read_csv(filename)
print((x.columns))
print(x.shape)
print(x)


y = x[0]['Type']
print(y)

#print(y.shape)




z = data_structure.dataFrame([['a','b','c'],[1,2,3],[2,4,5]])
print(z)
data_structure.dataFrame.save_as_csv(z,filename = 'data/prac1.csv')
#print(x.columns)
#Nishant Luitel is a Hero and Nobody can deny

