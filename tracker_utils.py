# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 19:59:32 2022

@author: acer
"""


from data_structure import dataFrame




def read_game_data(dataFolder, gameId):
    ''' returns 3-tuple of dataFrame of events data , tracking data of home team and tracking data of away team'''
    
    #filename_away_track = '/Sample_Game_{0}/Sample_Game_{0}_RawTrackingData_Away_Team.csv'.format(str(gameId))

    #filename_home_track = '/Sample_Game_{0}/Sample_Game_{0}_RawTrackingData_Home_Team.csv'.format(str(gameId))
        
    #tracking_data_home =  dataFrame(dataFolder + filename_home_track)
    #tracking_data_away =  dataFrame(dataFolder + filename_away_track)
    
    return (read_event_data(dataFolder,gameId),
            read_tracking_data(dataFolder,gameId, team='Home'),
            read_tracking_data(dataFolder,gameId, team='Away'))

    
def read_tracking_data(dataFolder, gameId , team):
    '''returns dataFrame of tracking data of Home team or Away team'''
    
    if team == 'Home' or team == 'Away':
        filename_track = '/Sample_Game_{0}/Sample_Game_{0}_RawTrackingData_{1}_Team.csv'.format(str(gameId),team)
    else:
        assert False, "team can be either 'Home' or 'Away'"
        
    tracking_data_dF =  dataFrame(dataFolder + filename_track)
    jerseys = get_player_jersey_from_tracking(tracking_data_dF)
    
    new_column_head = [tracking_data_dF[1].aslist[0], tracking_data_dF[1].aslist[1], tracking_data_dF[2].aslist[0]]
    for jersey in jerseys:
        new_column_head.append(str(jersey)+'_x')
        new_column_head.append(str(jersey)+'_y')
    new_column_head.append['Ball_x','Ball_y']
    
    tracking_data = dataFrame(tracking_data_dF,skiprows = 2)
    tracking_data.change_columnName(name = new_column_head)
    return tracking_data
    
    
    

def read_event_data(dataFolder , gameId):
    '''returns dataFrame of events data'''
    
    filename_events = '/Sample_Game_{0}/Sample_Game_{0}_RawEventsData.csv'.format(str(gameId))
    events_data =  dataFrame(dataFolder + filename_events)
    return events_data

def get_player_jersey_from_tracking(tracking_data_dF):
    '''returns a list of jersey numbers of players involved in the given team'''
    
    jerseys = tracking_data_dF[0].aslist
    jerseys = [int(item) for item in jerseys if item != '']
    return jerseys
    
    



    
    
    
    
    
    
