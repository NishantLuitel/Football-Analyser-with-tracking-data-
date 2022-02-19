# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 17:45:55 2022

@author: acer
"""



from visualize import plot_pitch,plot_frame
from data_structure import dataFrame
import tracker_utils
from calc import calculate_velocity
import os.path


dataFolder = 'data'
gameId = 2


events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId,to_metric = True)
events_home = events[events['Team'] == 'Home']
events_away = events[events['Team'] == 'Away']


filename = '/Sample_Game_{0}/to_metric/with_speed/Sample_Game_{0}_RawTrackingData_{1}_Team.csv'


#Can take few minutes to run for first time
for team,tracking in zip(['Home','Away'],[tracking_home,tracking_away]):
    with_speed_filename = filename.format(str(gameId),team)
    if os.path.isfile(dataFolder  + with_speed_filename):
        continue
    for jersey_no in tracker_utils.get_player_jersey_from_tracking(tracking):
        calculate_velocity(tracking,jersey_no,smoothing = True,save_to_tracking=True)
    dataFrame.save_as_csv(tracking,dataFolder + with_speed_filename)
tracking_home = dataFrame(dataFolder+filename.format(str(gameId),'Home'))
tracking_away = dataFrame(dataFolder+filename.format(str(gameId),'Away'))

start_frame = int(events[events['Subtype']=='KICK OFF']['Start Frame'].aslist[0]) + 1000+25
#start_frame = 20
fa = plot_pitch()
f,a = plot_frame(tracking_home[start_frame],tracking_away[start_frame],figax=fa, include_player_velocities=True,annotate = True)

