# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 18:16:25 2022

@author: acer
"""

from data_structure import dataFrame
import tracker_utils
from calc import goals, shots,distance_covered,passes_completed,passes_attempted,sprints,recoveries,interceptions,minutes_played,max_speed,challenges_won,challenges_lost,aerial_duals_lost,aerial_duals_won,fouls_recieved,completed_crosses,tackles_won,tackles_lost

dataFolder = 'data'
gameId = 1


events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId,to_metric = True)
#tracker_utils._to_metric(tracking_home)
#tracker_utils.to_metric(tracking_away)



#print(events.columns)
#print(tracking_home.columns)
#print(tracking_home)
#print(tracking_away)
#events['Type'].value_counts()
#events['Subtype'].value_counts()
#events['From'].value_counts()
#events[events['Type'] == 'BALL LOST']['Subtype'].value_counts()



events_home = events[events['Team'] == 'Home']
events_away = events[events['Team'] == 'Away']
#events_home[events_home['Type'] == 'BALL LOST']['Subtype'].value_counts()
#print(events_home)
#print('Home Events\n')
#events_home['Type'].value_counts()
#events_home['Subtype'].value_counts()
#events_home['From'].value_counts()
#events_away['From'].value_counts()




jersey_no = 9

print('\n\nStat Summery of home player',jersey_no)
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\nThe number of shots made by player',jersey_no,'is: ',shots(events_home,jersey_no))
print('The number of tackles won by player',jersey_no,'is: ',tackles_won(events_home,jersey_no))
print('%tackles won by player',jersey_no,'is: ',round(tackles_won(events_home,jersey_no)/(tackles_won(events_home,jersey_no) + tackles_lost(events_home,jersey_no)),2))
print('%challenges won accuracy by player',jersey_no,'is: ',round(challenges_won(events_home,jersey_no)/(challenges_won(events_home,jersey_no) + challenges_lost(events_home,jersey_no)),2))
print('%aerial dual won accuracy by player',jersey_no,'is: ',round(aerial_duals_won(events_home,jersey_no)/(aerial_duals_won(events_home,jersey_no) + aerial_duals_lost(events_home,jersey_no)),2))
print('Foul recieved by player',jersey_no,'is: ',fouls_recieved(events_home,jersey_no))
print('The number of passes completed by player',jersey_no,'is: ',passes_completed(events_home,jersey_no))
print('Pass accuracy by player',jersey_no,'is: ',round(passes_completed(events_home,jersey_no)/passes_attempted(events_home,jersey_no),2))
print('Crosses completed by player',jersey_no,'is: ',completed_crosses(events_home,jersey_no))
print('Ball Recoveries made by player',jersey_no,'is: ',recoveries(events_home,jersey_no))
print('Interceptions made by player',jersey_no,'is: ',interceptions(events_home,jersey_no))
print('Minutes played by player',   jersey_no,'is: ',minutes_played(tracking_home,jersey_no) )
print('Maximum speed(in kilometers/sec) reached by player',jersey_no,'is: ',round(max_speed(tracking_home,jersey_no),2))
print('Distance covered(in kilometers) by player',jersey_no,'is: ',round(distance_covered(tracking_home,jersey_no),2))
print('Sprints made by player',jersey_no,'is: ',sprints(tracking_home,jersey_no))
print('goals scored by player',jersey_no,'is: ',goals(events_home,jersey_no))




#subtype_strings = list(set(events_home[events_home['From'] == 'Player'+str(jersey_no)]['Subtype'].aslist))
#goal_strings = [goal_string for goal_string in subtype_strings if goal_string.endswith('-GOAL')]
#print(goal_strings)


#events_home[events_home['From'] == 'Player'+str(jersey_no)]['Subtype'].value_counts()

#speed = calculate_velocity(tracking_home,jersey_no)

#m = calculate_velocity(tracking_home,jersey_no,smoothing = True)
#dataFrame.save_as_csv(m, '11_smoothered8.csv')
#print(m)
