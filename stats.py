
"""
Run this module to create a stat summary of players for the game

"""

import data_structure 

import tracker_utils 
import calc
#import visualize
from calc import generate_passes_table,generate_avg_xy


dataFolder = 'data'
gameId = 1

events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder,gameId,to_metric = True)




events_home = events[events['Team'] == 'Home']
events_away = events[events['Team'] == 'Away']







table = generate_passes_table(tracking_away,events_away)
data_frame_table = data_structure.dataFrame(table)
data_structure.dataFrame.save_as_csv(data_frame_table,'passes_away.csv')


table2 = generate_avg_xy(tracking_away)
data_frame_table2 = data_structure.dataFrame(table2)
data_structure.dataFrame.save_as_csv(data_frame_table2,'avg1_away.csv')

table = generate_passes_table(tracking_home,events_home)
data_frame_table = data_structure.dataFrame(table)
data_structure.dataFrame.save_as_csv(data_frame_table,'passes_away.csv')


table2 = generate_avg_xy(tracking_home)
data_frame_table2 = data_structure.dataFrame(table2)
data_structure.dataFrame.save_as_csv(data_frame_table2,'avg1_home.csv')





#a,b=visualize.plot_pitch()

#dataFolder = 'data'
#gameId = 1


#events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId,to_metric = True)

# avg_home=calc.avg_position(tracking_home)
# print(avg_home["1_x"])

#events_home = events[events['Team'] == 'Home']
#events_away = events[events['Team'] == 'Away']

startingxihome_no=[]
playerno=tracker_utils.get_player_jersey_from_tracking(tracking_home)
for i in playerno:
    x=calc.__check_player_in_startingEleven(tracking_home,i)
    if x==True :
        startingxihome_no.append(i)
#print(*startingxihome_no)


startingxiaway_no=[]
playerno=tracker_utils.get_player_jersey_from_tracking(tracking_away)
for i in playerno:
    x=calc.__check_player_in_startingEleven(tracking_away,i)
    if x==True :
        startingxiaway_no.append(i)
        
# averagexhome_xi=[]
# for i in startingxihome_no:
#     string=i+"_x"
#     pos=avg_home[string]
#     averagexhome_xi.append(pos)
# print(*averagexhome_xi)
#shots for both home and away team


#SHOTS FOR BOTH HOME AND AWAY TEAM
shotshome_xi=[]
shotsaway_xi=[]
for i in startingxihome_no:
    shot=calc.shots(events_home,i)
    shotshome_xi.append(shot)
for i in startingxiaway_no:
    shot=calc.shots(events_away,i)
    shotsaway_xi.append(shot)
#print(*shotshome_xi)

#goals for both home and away team
goalshome_xi=[]
goalsaway_xi=[]
for i in startingxihome_no:
    goal=calc.goals(events_home,i)
    goalshome_xi.append(shot)
for i in startingxiaway_no:
    goal=calc.goals(events_away,i)
    goalsaway_xi.append(shot)
#print(*goalshome_xi)

#passes_completed for both home and away team
passes_completedhome_xi=[]
passes_completedaway_xi=[]
for i in startingxihome_no:
    passes=calc.passes_completed(events_home,i)
    passes_completedhome_xi.append(passes)
for i in startingxiaway_no:
    passes=calc.passes_completed(events_away,i)
    passes_completedaway_xi.append(passes)
print("\n PASSES \n")
#print(*passes_completedhome_xi)
#print(*passes_completedaway_xi)

#completed_crosses for both home and away team
completed_crosseshome_xi=[]
completed_crossesaway_xi=[]
for i in startingxihome_no:
    crosses=calc.completed_crosses(events_home,i)
    completed_crosseshome_xi.append(crosses)
for i in startingxiaway_no:
    crosses=calc.completed_crosses(events_away,i)
    completed_crossesaway_xi.append(crosses)
#print(*completed_crosseshome_xi)

#TACKLE WON FOR HOME AND AWAY TEAM   
tackles_wonhome_xi=[]
tackles_wonaway_xi=[]
for i in startingxihome_no:
    tackles=calc.tackles_won(events_home,i)
    tackles_wonhome_xi.append(tackles)
for i in startingxiaway_no:
    tackles=calc.tackles_won(events_away,i)
    tackles_wonaway_xi.append(tackles)
#print(*tackles_wonhome_xi)

#ARIEAL DUALS FOR HOME AND AWAY TEAM
aerial_duals_wonhome_xi=[]
aerial_duals_wonaway_xi=[]
for i in startingxihome_no:
    duels=calc.aerial_duals_won(events_home,i)
    aerial_duals_wonhome_xi.append(duels)
for i in startingxiaway_no:
    duels=calc.aerial_duals_won(events_away,i)
    aerial_duals_wonaway_xi.append(duels)
#print(*aerial_duals_wonhome_xi)


#fouls won for home and away team
# fouls_recievedhome_xi=[]
# fouls_recievedaway_xi=[]
# for i in startingxihome_no:
#     duelswon=calc.fouls_recieved(events_home,i)
#     fouls_recievedhome_xi.append(duelswon)
# for i in startingxiaway_no:
#     duelswon=calc.fouls_recieved(events_away,i)
#     fouls_recievedhome_xi.append(duelswon)

# print(*fouls_recievedhome_xi)

#  challenges_won for home and away team
challenges_wonhome_xi=[]
challenges_wonaway_xi=[]
for i in startingxihome_no:
    challengeswon=calc.challenges_won(events_home,i)
    challenges_wonhome_xi.append(challengeswon)
for i in startingxiaway_no:
    challengeswon=calc.challenges_won(events_away,i)
    challenges_wonaway_xi.append(challengeswon)
#print(*challenges_wonhome_xi)

#  interceptions for home and away team
# interceptionshome_xi=[]
# interceptionsaway_xi=[]
# for i in startingxihome_no:
#     interceptionswon=calc.interceptions(events_home,i)
#     interceptionshome_xi.append(interceptionswon)
# for i in startingxiaway_no:
#     interceptionswon=calc.interceptions(events_away,i)
#     interceptionsaway_xi.append(interceptionswon)

#  recoveries for home and away team
recoverieshome_xi=[]
recoveriesaway_xi=[]
for i in startingxihome_no:
    recoverieswon=calc.recoveries(events_home,i)
    recoverieshome_xi.append(recoverieswon)
for i in startingxiaway_no:
    recoverieswon=calc.recoveries(events_away,i)
    recoveriesaway_xi.append(recoverieswon)
#print(*recoverieshome_xi)

table_h=list(zip(startingxihome_no,shotshome_xi,passes_completedhome_xi,completed_crosseshome_xi,tackles_wonhome_xi,challenges_wonhome_xi,aerial_duals_wonhome_xi))
#table_home=[*zip(*table_h)]
table_a=list(zip(startingxiaway_no,shotsaway_xi,passes_completedaway_xi,completed_crossesaway_xi,tackles_wonaway_xi,challenges_wonaway_xi,aerial_duals_wonaway_xi))
#table_away=[*zip(*table_a)]


listofstats=["jerseyno","shots","passes completed","crosses completed","tackes won","challenges won","aerial duals won"]
table_h.insert(0,listofstats)
table_a.insert(0,listofstats)
d1=data_structure.dataFrame(table_h)
data_structure.dataFrame.save_as_csv(d1,"jackass.csv")




# s = [[str(e) for e in row] for row in table_h]
# lens = [max(map(len, col)) for col in zip(*s)]
# fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
# table = [fmt.format(*row) for row in s]
# print ('\n'.join(table))




#events_home[events_home['Type'] == 'BALL LOST']['Subtype'].value_counts()
#print(events_home)
#print('Home Events\n')
#events_home['Type'].value_counts()
#events_home['Subtype'].value_counts()
#events_home['From'].value_counts()
#events_away['From'].value_counts()




jersey_no = 9

print('\n\nStat Summery of home player',jersey_no)
# print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
print('\nThe number of shots made by player',jersey_no,'is: ',calc.shots(events_home,jersey_no))
print('The number of tackles won by player',jersey_no,'is: ',calc.tackles_won(events_home,jersey_no))
#print('%tackles won by player',jersey_no,'is: ',round(tackles_won(events_home,jersey_no)/(tackles_won(events_home,jersey_no) + tackles_lost(events_home,jersey_no)),2))
# print('%challenges won accuracy by player',jersey_no,'is: ',round(challenges_won(events_home,jersey_no)/(challenges_won(events_home,jersey_no) + challenges_lost(events_home,jersey_no)),2))
# print('%aerial dual won accuracy by player',jersey_no,'is: ',round(aerial_duals_won(events_home,jersey_no)/(aerial_duals_won(events_home,jersey_no) + aerial_duals_lost(events_home,jersey_no)),2))
# print('Foul recieved by player',jersey_no,'is: ',fouls_recieved(events_home,jersey_no))
print('The number of passes completed by player',jersey_no,'is: ',calc.passes_completed(events_home,jersey_no))
# print('Pass accuracy by player',jersey_no,'is: ',round(passes_completed(events_home,jersey_no)/passes_attempted(events_home,jersey_no),2))
# print('Crosses completed by player',jersey_no,'is: ',completed_crosses(events_home,jersey_no))
# print('Ball Recoveries made by player',jersey_no,'is: ',recoveries(events_home,jersey_no))
print('Interceptions made by player',jersey_no,'is: ',calc.interceptions(events_home,jersey_no))
# print('Minutes played by player',   jersey_no,'is: ',minutes_played(tracking_home,jersey_no) )
# print('Maximum speed(in kilometers/sec) reached by player',jersey_no,'is: ',round(max_speed(tracking_home,jersey_no),2))
# print('Distance covered(in kilometers) by player',jersey_no,'is: ',round(distance_covered(tracking_home,jersey_no),2))
# print('Sprints made by player',jersey_no,'is: ',sprints(tracking_home,jersey_no))
# print('goals scored by player',jersey_no,'is: ',goals(events_home,jersey_no))

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



'''

Run this module to create a stat summary of players for the game


from data_structure import dataFrame
import tracker_utils
from calc import goals, shots,distance_covered,passes_completed
from calc import passes_attempted,sprints,recoveries,interceptions,minutes_played
from calc import max_speed,challenges_won,challenges_lost
from calc import aerial_duals_won, aerial_duals_lost,fouls_recieved,completed_crosses,tackles_won,tackles_lost
from calc import calculate_at_once,passes,avg_position,generate_passes_table,generate_avg_xy


dataFolder = 'data'
gameId = 1

events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder,gameId,to_metric = True)




events_home = events[events['Team'] == 'Home']
events_away = events[events['Team'] == 'Away']





jersey_no = 11


#table = generate_passes_table(tracking_away,events_away)
#data_frame_table = dataFrame(table)
#dataFrame.save_as_csv(data_frame_table,'passes2.csv')

#print(passes(7,10,events_home))


#table2 = generate_avg_xy(tracking_away)
#data_frame_table2 = dataFrame(table2)
#dataFrame.save_as_csv(data_frame_table2,'avg2.csv')

#print(avg_home['5_x'])

#print(passes(5,2,events))
#print(events_home['Type'])


#print('\n\nStat Summary of home player',jersey_no)
#print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
#print('\nThe number of shots made by player',jersey_no,'is: ',shots(events_home,jersey_no))
#print('The number of tackles won by player',jersey_no,'is: ',tackles_won(events_home,jersey_no))
#print('%tackles won by player',jersey_no,'is: ',round(tackles_won(events_home,jersey_no)/(tackles_won(events_home,jersey_no) + tackles_lost(events_home,jersey_no)),2))
#print('%challenges won accuracy by player',jersey_no,'is: ',round(challenges_won(events_home,jersey_no)/(challenges_won(events_home,jersey_no) + challenges_lost(events_home,jersey_no)),2))
#print('%aerial dual won accuracy by player',jersey_no,'is: ',round(aerial_duals_won(events_home,jersey_no)/(aerial_duals_won(events_home,jersey_no) + aerial_duals_lost(events_home,jersey_no)),2))
#print('Foul recieved by player',jersey_no,'is: ',fouls_recieved(events_home,jersey_no))
#print('The number of passes completed by player',jersey_no,'is: ',passes_completed(events_home,jersey_no))
#print('Pass accuracy by player',jersey_no,'is: ',round(passes_completed(events_home,jersey_no)/passes_attempted(events_home,jersey_no),2))
#print('Crosses completed by player',jersey_no,'is: ',completed_crosses(events_home,jersey_no))
#print('Ball Recoveries made by player',jersey_no,'is: ',recoveries(events_home,jersey_no))
#print('Interceptions made by player',jersey_no,'is: ',interceptions(events_home,jersey_no))
#print('Minutes played by player',   jersey_no,'is: ',minutes_played(tracking_home,jersey_no) )
#tup = calculate_at_once(tracking_home,jersey_no)
#print('-Maximum speed(in kilometers/sec) reached by player',jersey_no,'is: ',round(max_speed(tracking_home,jersey_no),2))
#print('Maximum speed(in kilometers/sec) reached by player',jersey_no,'is: ',round(tup[0],2))
#print('-Distance covered(in kilometers) by player',jersey_no,'is: ',round(distance_covered(tracking_home,jersey_no),2))
#print('Distance covered(in kilometers) by player',jersey_no,'is: ',round(tup[1],2))
#print('-Sprints made by player',jersey_no,'is: ',sprints(tracking_home,jersey_no))
#print('Sprints made by player',jersey_no,'is: ',tup[2])
#print('goals scored by player',jersey_no,'is: ',goals(events_home,jersey_no))


#print('GoalKeeper of home team is:',tracker_utils.get_goal_keeper_from_tracking(tracking_home))


    
    
    
    
    '''
