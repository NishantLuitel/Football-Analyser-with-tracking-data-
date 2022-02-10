# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:16:25 2022

@author: acer
"""


import tracker_utils
from calc import shots,passes_completed,passes_attempted

dataFolder = 'data'
gameId = 1


events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId)




print(events)
#print(tracking_home)
#print(tracking_away)
#events['Type'].value_counts()
#events['Subtype'].value_counts()
#events['From'].value_counts()
#events[events['Type'] == 'BALL LOST']['Subtype'].value_counts()


#events_home = events[events['Team'] == 'Home']
events_away = events[events['Team'] == 'Away']
#print(events_home)
#print('Home Events\n')
#events_home['Type'].value_counts()
#events_home['Subtype'].value_counts()
#events_home['From'].value_counts()
events_away['From'].value_counts()




jersey_no = 22
print('\nThe number of shots made by player',jersey_no,'is',shots(events_away,jersey_no))
print('\nThe number of passes completed by player',jersey_no,'is',passes_completed(events_away,jersey_no))
print('\nThe number of passes_attempted by player',jersey_no,'is',passes_attempted(events_away,jersey_no))
print('\nPass accuracy by player',jersey_no,'is',passes_completed(events_away,jersey_no)/
      passes_attempted(events_away,jersey_no))



