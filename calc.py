# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:59:07 2022

@author: acer
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
    
    return eventsCount(events,jersey_no,Type = 'Shots')
    

    
def passes_completed(events,jersey_no):
    '''Calulates the number of passes completed by player with 
    given jersey number in the given events data structure'''
    
    return eventsCount(events,jersey_no,Type = 'Pass')
    
    
    
def passes_attempted(events,jersey_no):
    '''Calulates the number of passes attemted by player with 
    given jersey number in the given events data structure'''
    
    #add the completed pass and the balls lost except by theft, clearances and shots 
    completed_passes = passes_completed(events,jersey_no)
    balls_lost = eventsCount(events,jersey_no,Type = 'Ball Lost')   
    balls_lostByTheft = Sub_eventsCount(events,jersey_no,Type = 'Theft') 
    balls_lostByHeadClearance = Sub_eventsCount(events,jersey_no,Type = 'Head-Clearance')
    balls_lostByClearance = Sub_eventsCount(events,jersey_no,Type = 'Clearance')
    balls_lostByWoodwork = Sub_eventsCount(events,jersey_no,Type = 'Woodwork')

    return (completed_passes + balls_lost - balls_lostByTheft - 
            balls_lostByClearance - balls_lostByHeadClearance -balls_lostByWoodwork)


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
    
    pass

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
    
    speed = calculate_velocity(tracking,jersey_no,smoothing = True)
    
    #because 1st value is a nan we max only elements after that
    return max(speed.aslist[1:])*3.60
    
    
    

def __check_player_in_tracking(tracking,jersey_no):
    
    player_str = str(jersey_no)+'_x'
    assert player_str in tracking.columns , "Player " + str(jersey_no) + " not present in the team"
    
def __check_player_in_startingEleven(tracking,jersey_no):
    
    player_str = str(jersey_no)+'_x'
    if tracking[player_str][0] == 'NaN':
        return False
    else:
        return True
    

    