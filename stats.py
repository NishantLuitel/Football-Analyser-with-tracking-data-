'''

Run this module to create a stat summary of players for the game

'''

from data_structure import dataFrame
import tracker_utils
from calc import goals, shots,distance_covered,passes_completed
from calc import passes_attempted,sprints,recoveries,interceptions,minutes_played
from calc import max_speed,challenges_won,challenges_lost
from calc import aerial_duals_won, aerial_duals_lost,fouls_recieved,completed_crosses,tackles_won,tackles_lost
from calc import calculate_at_once

dataFolder = 'data'
gameId = 1


events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId,to_metric = True)




events_home = events[events['Team'] == 'Home']
events_away = events[events['Team'] == 'Away']





jersey_no = 2


print('\n\nStat Summary of home player',jersey_no)
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
tup = calculate_at_once(tracking_home,jersey_no)
#print('-Maximum speed(in kilometers/sec) reached by player',jersey_no,'is: ',round(max_speed(tracking_home,jersey_no),2))
print('Maximum speed(in kilometers/sec) reached by player',jersey_no,'is: ',round(tup[0],2))
#print('-Distance covered(in kilometers) by player',jersey_no,'is: ',round(distance_covered(tracking_home,jersey_no),2))
print('Distance covered(in kilometers) by player',jersey_no,'is: ',round(tup[1],2))
#print('-Sprints made by player',jersey_no,'is: ',sprints(tracking_home,jersey_no))
print('Sprints made by player',jersey_no,'is: ',tup[2])
print('goals scored by player',jersey_no,'is: ',goals(events_home,jersey_no))


#print('GoalKeeper of home team is:',tracker_utils.get_goal_keeper_from_tracking(tracking_home))


