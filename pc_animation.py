
'''
This module is used to animate the goal scenes with pitch control and store it to default location animations/pitch_control '' 

For simple goal scene animations see goal_animation.py

Note: Creating pitch control animation is time consuming
'''


from visualize import save_pitch_control_clip
from data_structure import dataFrame
from pitch_control import default_model_params
import tracker_utils
from calc import calculate_velocity
import os.path

#Folder where sample data is placed and the game id
dataFolder = 'data'
gameId = 2


events,tracking_home,tracking_away = tracker_utils.read_game_data(dataFolder, gameId,to_metric = True)

#gate events for home and away team seperately
events_home = events[events['Team'] == 'Home']
events_away = events[events['Team'] == 'Away']


filename = '/Sample_Game_{0}/to_metric/with_speed/Sample_Game_{0}_RawTrackingData_{1}_Team.csv'


#Read the game events and tracking data with velocity calculated
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


#Calculate the frames in which games occur
#Similar frame returning function for other events can be created
def goal_indexes(events):
    
    subtype_strings = list(set(events['Subtype'].aslist))
    goal_strings = [goal_string for goal_string in subtype_strings if goal_string.endswith('-GOAL')]
    frames = []
    if len(goal_strings) > 0:
        for goal_string in goal_strings:
            if type(events[events['Subtype'] == goal_string]['Start Frame']) != str and type(events[events['Subtype'] == goal_string]['Start Frame']) != int:
                frames+= events[events['Subtype'] == goal_string]['Start Frame'].aslist
            else:
                frames.append(events[events['Subtype'] == goal_string]['Start Frame'])
    return [int(frame) for frame in sorted(frames,key = int)]


#Some parameters required to generate the model
params = default_model_params()
GKnumbers = [tracker_utils.get_goal_keeper_from_tracking(tracking_home),tracker_utils.get_goal_keeper_from_tracking(tracking_away)]


####Code for creating videos for all goals for given gameId with pitch control
name= {0:'Home' , 1:'Away'}
i = 0
for events in (events_home,events_away):
    temp_filename = name[i]
    if gameId>1:
        temp_filename = str(gameId)+temp_filename
    if len(goal_indexes(events))>0:
        frames = goal_indexes(events)
        j = 1
        for frame in frames:
            filename= temp_filename + ('_'+str(j))
            j+=1
            start_frame = frame - 625 
            end_frame = frame + 250
            goal_index_list = list(range(start_frame,end_frame))
            save_pitch_control_clip(events = events ,hometeam = tracking_home[goal_index_list] ,awayteam = tracking_away[goal_index_list],fname = filename,GKnumbers = GKnumbers,params = params, include_player_velocities=True,annotate=True)            
    i+=1




