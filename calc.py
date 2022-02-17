# -*- coding: utf-8 -*-
"""

This module consists of all the calculations required for this project

"""

import numpy as np
#This module consists of all the calculations required for the project

    
def eventsCount(events,jersey_no,Type):
    '''Calulates the number of given event type completed by player with 
    given jersey number in the given events data structure'''
    
    string = 'Player'+str(jersey_no)
    eventType_index = events[events['From'] == string]['Type'] == Type.upper()
    if eventType_index != False:
        return len(eventType_index)
    else:
        return 0
 
    
def Sub_eventsCount(events,jersey_no,Type):
    '''Calulates the number of given sub-event type completed by player with 
    given jersey number in the given events data structure'''
    
    string = 'Player'+str(jersey_no)
    eventType_index = events[events['From'] == string]['Subtype'] == Type.upper()
    if eventType_index != False:
        return len(eventType_index)
    else:
        return 0

    
def shots(events,jersey_no):
    '''Calulates the number of shots taken by player with 
    given jersey number in the given events data structure'''
    
    return eventsCount(events,jersey_no,Type = 'Shot')

    
def goals(events,jersey_no):
    '''Calulates the number of goals scored by player with 
    given jersey number in the given events data structure'''
    
    #first find all the subtypes strings that ends in -GOAL
    string = 'Player'+str(jersey_no)
    subtype_strings = list(set(events[events['From'] == string]['Subtype'].aslist))
    goal_strings = [goal_string for goal_string in subtype_strings if goal_string.endswith('-GOAL')]
    num_goals = 0
    
    #Sum over all the type of goals
    for goal_string in goal_strings:
        num_goals+=Sub_eventsCount(events,jersey_no,Type=goal_string)
    
    return num_goals


def completed_crosses(events,jersey_no):
    '''Calulates the number of completed crosses by player with 
    given jersey number in the given events data structure'''
    
    #Only crosses during pass are considered(no setpiece crosses and corner kick crosses) 
    return Sub_eventsCount(events,jersey_no,Type = 'Cross')
    
 
   
def passes_completed(events,jersey_no):
    '''Calulates the number of passes completed by player with 
    given jersey number in the given events data structure'''
    
    return eventsCount(events,jersey_no,Type = 'Pass')
    
        
def passes_attempted(events,jersey_no):
    '''Calulates the number of passes attemted by player with 
    given jersey number in the given events data structure'''
     
    completed_passes = passes_completed(events,jersey_no)
    balls_lost = eventsCount(events,jersey_no,Type = 'Ball Lost')   
    balls_lostByTheft = Sub_eventsCount(events,jersey_no,Type = 'Theft') 
    balls_lostByHeadClearance = Sub_eventsCount(events,jersey_no,Type = 'Head-Clearance')
    balls_lostByClearance = Sub_eventsCount(events,jersey_no,Type = 'Clearance')
    balls_lostByWoodwork = Sub_eventsCount(events,jersey_no,Type = 'Woodwork')

    return (completed_passes + balls_lost - balls_lostByTheft - 
            balls_lostByClearance - balls_lostByHeadClearance -balls_lostByWoodwork)


def tackles_won(events,jersey_no):
    '''Calulates the number of tackles won by player with 
    given jersey number in the given events data structure'''
    
    return Sub_eventsCount(events,jersey_no,Type = 'TACKLE-WON')


def tackles_lost(events,jersey_no):
    '''Calulates the number of tackles lost by player with 
    given jersey number in the given events data structure'''
    
    return Sub_eventsCount(events,jersey_no,Type = 'TACKLE-LOST')


def aerial_duals_won(events,jersey_no):
    '''Calulates the number of aerial duals won by player with 
    given jersey number in the given events data structure'''
    
    return Sub_eventsCount(events,jersey_no,Type = 'AERIAL-WON')


def aerial_duals_lost(events,jersey_no):
    '''Calulates the number of aerial duals lost by player with 
    given jersey number in the given events data structure'''
    
    return Sub_eventsCount(events,jersey_no,Type = 'AERIAL-LOST')


def fouls_recieved(events,jersey_no):
    '''Calulates the number of aerial duals lost by player with 
    given jersey number in the given events data structure'''
    
    return eventsCount(events,jersey_no,Type = 'FAULT RECIEVED')


def challenges_won(events,jersey_no):
    '''Calulates the number of challenges won by player with 
    given jersey number in the given events data structure'''
    
    string = 'Player'+str(jersey_no)
    subtype_strings = list(set(events[events['From'] == string]['Subtype'].aslist))
    challenge_won_strings = [challenge_won_string for challenge_won_string in subtype_strings if challenge_won_string.endswith('-WON')]
    num_challenges_won = 0
    
    #Sum over all the type of won challenges
    for challenge_won_string in challenge_won_strings:
        num_challenges_won+=Sub_eventsCount(events,jersey_no,Type=challenge_won_string)
    
    return num_challenges_won


def challenges_lost(events,jersey_no):
    '''Calulates the number of challenges lost by player with 
    given jersey number in the given events data structure'''
    
    string = 'Player'+str(jersey_no)
    subtype_strings = list(set(events[events['From'] == string]['Subtype'].aslist))
    challenge_lost_strings = [challenge_lost_string for challenge_lost_string in subtype_strings if challenge_lost_string.endswith('-LOST')]
    num_challenges_lost = 0
    
    #Sum over all the type of lost challenges
    for challenge_lost_string in challenge_lost_strings:
        num_challenges_lost+=Sub_eventsCount(events,jersey_no,Type=challenge_lost_string)
    
    return num_challenges_lost

    
def interceptions(events,jersey_no):
    '''Calulates the number of interceptions made by player with 
    given jersey number in the given events data structure'''
    
    recovery_events = events[events['Type'] == 'RECOVERY']
    return Sub_eventsCount(recovery_events,jersey_no,'Interception')

    
def recoveries(events,jersey_no):
    '''Calulates the number of recoveries made by player with 
    given jersey number in the given events data structure'''
    
    return eventsCount(events,jersey_no,'Recovery')


def minutes_played(tracking,jersey_no):
    '''Calculates the minutes played by player of given jersey number'''
    
    __check_player_in_tracking(tracking, jersey_no)
    player_str = str(jersey_no)+'_x'
    
    #Each index lasts 1/25 seconds , hence we divide by 25
    #We also divide by 60 to get value in minutes
    if (__check_player_in_startingEleven(tracking,jersey_no)):
        try:
            return round(float(tracking[player_str].find_last_validOfTwo()+ 1)/25/60,2)
        
        #Assertion error occurs if there no invalid item is present i.e. player plays full minutes
        except AssertionError:
            return round(float(len(tracking[player_str].aslist))/25/60,2)
    else:
        #Takes longer time to execute
        return round(float(len(tracking[player_str] != 'NaN'))/25/60,2)


def distance_covered(tracking,jersey_no):
    '''Calculates the distace covered (in kilometers) by given jersey number'''
    
    speed = calculate_velocity(tracking,jersey_no)
    dt = tracking['Time [s]'].diff().aslist[1] 
    #distance covered is speed multiplied time and summed over
    #divide by 1000 to convert into kilometers
    distance = round((speed.sum()*dt)/1000,4)
    
    return distance


def calculate_velocity(tracking,jersey_no,smoothing = False,window_size = 5,max_speed = 12.0 ,save_to_tracking=False):
    '''Calulates velocity for player of given jersey_no. (in m/sec)
    
        Convolution is done of given window size if smoothing is set to True'''
        
    assert max_speed>0, "speed should only have magnitude"   
    player_str_x = str(jersey_no)+'_x'
    player_str_y = str(jersey_no)+'_y'
    
    
    first_half_idx = (tracking['Period'] == '1')
    second_half_idx = (tracking['Period'] == '2')
    #second_half_idx = tracking['Period'].find_last_validOfTwo('2')
    dt = tracking['Time [s]'].diff().aslist[1]
    
    #Calculate velocity in x and y direction
    vx = tracking[player_str_x].diff()/dt
    vy = tracking[player_str_y].diff()/dt
    
    
    speed = (vx**2 + vy**2)**(0.5) 
    speed.change_columnName([str(jersey_no) + "_speed"])
    vx[speed>max_speed] = float('NaN')
    vx[speed>max_speed] = float('NaN')

    
    if smoothing == True:
        window = [1/window_size]*window_size
        vx[first_half_idx] = list(np.convolve(vx[first_half_idx].aslist , window ,'same'))
        vx[second_half_idx] = list(np.convolve(vx[second_half_idx].aslist , window ,'same'))
        
        vy[first_half_idx] = list(np.convolve(vy[first_half_idx].aslist , window ,'same'))
        vy[second_half_idx] = list(np.convolve(vy[second_half_idx].aslist , window ,'same'))

    speed = (vx**2 + vy**2)**(0.5) 
    if save_to_tracking == True:
        tracking[str(jersey_no) + "_vx"] = vx.aslist
        tracking[str(jersey_no) + "_vy"] = vy.aslist
        tracking[str(jersey_no) + "_speed"] = speed.aslist
    
    return speed

    
def max_speed(tracking,jersey_no):
    '''Returns the maximum speed (in kilometers/hour) reached by player of given jersey number'''
    
    #dt here is 0.04 seconds
    dt = tracking['Time [s]'].diff().aslist[1]
        
    #Maximum speed is the maximum of the average speed for each second for the player
    #That is why the window size is taken as 25 so that 0.04sec * 25 = 1sec 
    speed = calculate_velocity(tracking,jersey_no,window_size = int(1/dt) ,smoothing = True)
    
    #because 1st value is a nan we max only elements after that
    return max(speed.aslist[25:])*3.60
    

def sprints(tracking,jersey_no):
    '''Returns the number of sprints made by player
        Note: Sprints occur when a player moves with speed greater than 7m/s for at least a second'''
        
    speed = calculate_velocity(tracking,jersey_no,smoothing = True)
    sprint_threshold = 7.0
    dt = tracking['Time [s]'].diff().aslist[1]
    sprint_window = int(1/dt)
    window = [1]*sprint_window
    
    #Creating a list with 1 where speed is greater than sprint threshold and 0 where less than sprint threshold
    sprint_threshold_index = (speed > sprint_threshold)
    sprint_bools = [0]*speed.num_rows
    for i in sprint_threshold_index : sprint_bools[i] = 1
        
    #
    temp_list = np.convolve(sprint_bools,window,mode = 'same')
    player_sprints = [0]*speed.num_rows
    for i in range(len(player_sprints)): player_sprints[i] = (1 if (temp_list[i] >= sprint_window) else 0)
    diff_player_sprints = [player_sprints[i+1]-player_sprints[i] for i in range(len(player_sprints)-1) if(player_sprints[i+1] - player_sprints[i])>0]
    
    return sum(diff_player_sprints)

    
def __check_player_in_tracking(tracking,jersey_no):
    
    player_str = str(jersey_no)+'_x'
    assert player_str in tracking.columns , "Player " + str(jersey_no) + " not present in the team"
    
    
def __check_player_in_startingEleven(tracking,jersey_no):
    
    player_str = str(jersey_no)+'_x'
    if tracking[player_str][0] == 'NaN':
        return False
    else:
        return True
    
    

    