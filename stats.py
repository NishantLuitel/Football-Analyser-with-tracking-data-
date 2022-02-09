# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:16:25 2022

@author: acer
"""


import tracker_utils

dataFolder = 'data'
gameId = 1


events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId)




print(events)
print(tracking_home)
print(tracking_away)
events['Type'].value_counts()
events['Subtype'].value_counts()
events['From'].value_counts()

events_home = events[events['Team'] == 'Home']
print(events_home)
print('Home Events\n')
events_home['Type'].value_counts()
events_home['Subtype'].value_counts()
events_home['From'].value_counts()

def shots(events,jersey_no):
    string = 'Player'+str(jersey_no)
    shts = len(events[events['From'] == string]['Type'] == 'SHOT')
    return shts


jersey_no = 13
print('\nThe number of shots made by player',jersey_no,'is',shots(events_home,jersey_no))
