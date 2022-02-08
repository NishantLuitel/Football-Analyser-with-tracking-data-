# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:16:25 2022

@author: acer
"""


import tracker_utils

dataFolder = 'data'
gameId = 2


e,th,ta = tracker_utils.read_game_data(dataFolder, gameId)

#print(th)
#print(ta)
print(e)
print(th)
print(ta)