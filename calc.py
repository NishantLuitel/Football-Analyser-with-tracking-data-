# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 19:59:07 2022

@author: acer
"""


#This module consists of all the calculations required for the project


def shots(events,jersey_no):
    '''Calulates the number of shots taken by player with 
    given jersey number in the given events data structure'''
    
    string = 'Player'+str(jersey_no)
    shts_index = events[events['From'] == string]['Type'] == 'SHOT'
    if shts_index != False:
        return len(shts_index)
    else:
        return 0

    
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
 
    
def passes_completed(events,jersey_no):
    '''Calulates the number of passes completed by player with 
    given jersey number in the given events data structure'''
    
    string = 'Player'+str(jersey_no)
    passes_index = events[events['From'] == string]['Type'] == 'PASS'
    if passes_index != False:
        return len(passes_index)
    else:
        return 0
    
    
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
    
