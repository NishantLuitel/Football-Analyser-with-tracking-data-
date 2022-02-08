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
file = 'data/prac1.csv'



 
#x = data_structure.dataFrame(filename)
#y = pd.read_csv(filename)
#print((x.columns))
#print(x.shape)
#print(x)


#y = x[0]['Type']
#print(y)

#print(y.shape)




#z = data_structure.dataFrame([['a','b','c'],[1,2,3],[2,4,5]])
#print(z)
#data_structure.dataFrame.save_as_csv(z,filename = 'data/prac1.csv')
#print(x.columns)

m = data_structure.dataFrame(filename_home_track)
#print(m['a'])
#print(m['a'][1])
#print(m[1])
#print(m[1]['a'])
#m['a'] = [7,8]
#print(m)
#m[1] = [0,3,0]
#print(m)
#m['a'][1] = 2
#print(m)

#print(m['a'])
#print(m['a', 1])
#m['a'][1] = 7
#m[0]['b'] = 7
#print(m)

#x = m[1]
#print(x)
#x[0]['a'] = 4
print(m)



