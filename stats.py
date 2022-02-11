# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:16:25 2022

@author: acer
"""


import tracker_utils
from calc import shots,passes_completed,passes_attempted,recoveries,interceptions

dataFolder = 'data'
gameId = 1


events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId,to_metric = True)
#tracker_utils._to_metric(tracking_home)
#tracker_utils.to_metric(tracking_away)



print(events.columns)
print(tracking_home.columns)
print(tracking_home)
#print(tracking_away)
#events['Type'].value_counts()
#events['Subtype'].value_counts()
#events['From'].value_counts()
#events[events['Type'] == 'BALL LOST']['Subtype'].value_counts()


#events_home = events[events['Team'] == 'Home']
#events_away = events[events['Team'] == 'Away']
#print(events_home)
#print('Home Events\n')
#events_home['Type'].value_counts()
#events_home['Subtype'].value_counts()
#events_home['From'].value_counts()
#events_away['From'].value_counts()




#jersey_no = 11
#print('\nThe number of shots made by player',jersey_no,'is',shots(events_home,jersey_no))
#print('The number of passes completed by player',jersey_no,'is',passes_completed(events_home,jersey_no))
#print('The number of passes attempted by player',jersey_no,'is',passes_attempted(events_home,jersey_no))
#print('Pass accuracy by player',jersey_no,'is',passes_completed(events_home,jersey_no)/
#      passes_attempted(events_home,jersey_no))
#events_home[events_home['Type'] == 'RECOVERY']['From'].value_counts()
#print('\nRecovery made by player',jersey_no,interceptions(events_home,jersey_no))



