# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:59:07 2022

@author: acer
"""


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
            return round(float(tracking[player_str].find_last_validOfTwo())/25/60,2)
        except AssertionError:
            return round(float(len(tracking[player_str].aslist))/25/60,2)
    else:
        #Takes longer time to execute
        return round(float(len(tracking[player_str] != 'NaN'))/25/60,2)
       #elif(tracking[player_str].find_last_valid()==0)
    
    #Assertion error occurs if there no invalid item is present i.e. player plays full minutes
    


def distance_covered(tracking,jersey_no):
    '''Calculates the distace covereed (in kilometers) by given jersey number'''
    
    pass

def __check_player_in_tracking(tracking,jersey_no):
    
    player_str = str(jersey_no)+'_x'
    assert player_str in tracking.columns , "Player " + str(jersey_no) + " not present in the team"
    
def __check_player_in_startingEleven(tracking,jersey_no):
    
    player_str = str(jersey_no)+'_x'
    if tracking[player_str][0] == 'NaN':
        return False
    else:
        return True
    
    
    