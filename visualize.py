
'''
This module consists of all the visualization tools needed for this project

'''


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math
from pitch_control import generate_pitch_control_for_frame



def plot_pitch( field_dimen = (105.0,68.0), field_color ='green', linewidth=2, markersize=15):
    
    '''
    Plots football pitch of given field dimension and returs (fig , axis) that can be used to
    to draw other things on the top of the pitch
        
    Credit: This Function is imported from Metrica_PitchControl.py made availabe by Friends Of Tracking community
        
    '''
    
    
    fig,ax = plt.subplots(figsize=(12,8)) # create a figure 
    # decide what color we want the field to be. Default is green, but can also choose white
    if field_color=='green':
        ax.set_facecolor('mediumseagreen')
        lc = 'whitesmoke' # line color
        pc = 'w' # 'spot' colors
    elif field_color=='white':
        lc = 'k'
        pc = 'k'
    # ALL DIMENSIONS IN m
    border_dimen = (3,3) # include a border arround of the field of width 3m
    meters_per_yard = 0.9144 # unit conversion from yards to meters
    half_pitch_length = field_dimen[0]/2. # length of half pitch
    half_pitch_width = field_dimen[1]/2. # width of half pitch
    signs = [-1,1] 
    # Soccer field dimensions typically defined in yards, so we need to convert to meters
    goal_line_width = 8*meters_per_yard
    box_width = 20*meters_per_yard
    box_length = 6*meters_per_yard
    area_width = 44*meters_per_yard
    area_length = 18*meters_per_yard
    penalty_spot = 12*meters_per_yard
    corner_radius = 1*meters_per_yard
    D_length = 8*meters_per_yard
    D_radius = 10*meters_per_yard
    D_pos = 12*meters_per_yard
    centre_circle_radius = 10*meters_per_yard
    # plot half way line # center circle
    ax.plot([0,0],[-half_pitch_width,half_pitch_width],lc,linewidth=linewidth)
    ax.scatter(0.0,0.0,marker='o',facecolor=lc,linewidth=0,s=markersize)
    y = np.linspace(-1,1,50)*centre_circle_radius
    x = np.sqrt(centre_circle_radius**2-y**2)
    ax.plot(x,y,lc,linewidth=linewidth)
    ax.plot(-x,y,lc,linewidth=linewidth)
    for s in signs: # plots each line seperately
        # plot pitch boundary
        ax.plot([-half_pitch_length,half_pitch_length],[s*half_pitch_width,s*half_pitch_width],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length],[-half_pitch_width,half_pitch_width],lc,linewidth=linewidth)
        # goal posts & line
        ax.plot( [s*half_pitch_length,s*half_pitch_length],[-goal_line_width/2.,goal_line_width/2.],pc+'s',markersize=6*markersize/20.,linewidth=linewidth)
        # 6 yard box
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*box_length],[box_width/2.,box_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*box_length],[-box_width/2.,-box_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length-s*box_length,s*half_pitch_length-s*box_length],[-box_width/2.,box_width/2.],lc,linewidth=linewidth)
        # penalty area
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*area_length],[area_width/2.,area_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length,s*half_pitch_length-s*area_length],[-area_width/2.,-area_width/2.],lc,linewidth=linewidth)
        ax.plot([s*half_pitch_length-s*area_length,s*half_pitch_length-s*area_length],[-area_width/2.,area_width/2.],lc,linewidth=linewidth)
        # penalty spot
        ax.scatter(s*half_pitch_length-s*penalty_spot,0.0,marker='o',facecolor=lc,linewidth=0,s=markersize)
        # corner flags
        y = np.linspace(0,1,50)*corner_radius
        x = np.sqrt(corner_radius**2-y**2)
        ax.plot(s*half_pitch_length-s*x,-half_pitch_width+y,lc,linewidth=linewidth)
        ax.plot(s*half_pitch_length-s*x,half_pitch_width-y,lc,linewidth=linewidth)
        # draw the D
        y = np.linspace(-1,1,50)*D_length # D_length is the chord of the circle that defines the D
        x = np.sqrt(D_radius**2-y**2)+D_pos
        ax.plot(s*half_pitch_length-s*x,y,lc,linewidth=linewidth)
        
    # remove axis labels and ticks
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_yticks([])
    # set axis limits
    xmax = field_dimen[0]/2. + border_dimen[0]
    ymax = field_dimen[1]/2. + border_dimen[1]
    ax.set_xlim([-xmax,xmax])
    ax.set_ylim([-ymax,ymax])
    ax.set_axisbelow(True)
    return fig,ax

def plot_frame( hometeam, awayteam, figax=None, team_colors=('b','r'), field_dimen = (105.0,68.0), include_player_velocities=False, PlayerMarkerSize=10, PlayerAlpha=0.7, annotate=False ):

    ''''
    Plots the player on top of pitch for given row of tracking_data as a dataFrame
    
    Credit: This function is slightly modified version from Metrica_Viz.py made available by Friends Of Tracking community
          that works for our dataFrame object
    
    '''
    
    if figax is None: # create new pitch 
        fig,ax = plot_pitch( field_dimen = field_dimen )
    else: # overlay on a previously generated pitch
        fig,ax = figax # unpack tuple
    # plot home & away teams in order
    for team,color in zip( [hometeam,awayteam], team_colors) :
        x_columns = [c for c in team.columns if c[-2:].lower()=='_x' and c.lower()!='ball_x'] # column header for player x positions
        y_columns = [c for c in team.columns if c[-2:].lower()=='_y' and c.lower()!='ball_y'] # column header for player y positions
        
        ax.plot( [float(team[column_name]) for column_name in x_columns if not math.isnan(float(team[column_name]))], [float(team[column_name]) for column_name in y_columns if not math.isnan(float(team[column_name]))], color+'o', markersize=PlayerMarkerSize, alpha=PlayerAlpha ) # plot player positions
        if include_player_velocities:
            vx_columns = ['{}_vx'.format(c[:-2]) for c in x_columns] # column header for player x positions
            vy_columns = ['{}_vy'.format(c[:-2]) for c in y_columns] # column header for player y positions
            ax.quiver( [float(team[column_name]) for column_name in x_columns],[float(team[column_name]) for column_name in y_columns], [float(team[column_name]) for column_name in vx_columns], [float(team[column_name]) for column_name in vy_columns], color=color, scale_units='inches', scale=10.,width=0.0015,headlength=5,headwidth=3,alpha=PlayerAlpha)
        if annotate:
            [ ax.text( float(team[x])+0.5, float(team[y])+0.5, x.split('_')[0], fontsize=10, color=color  ) for x,y in zip(x_columns,y_columns) if not ( np.isnan(float(team[x])) or np.isnan(float(team[y])) ) ] 
    # plot ball
    ax.plot( float(hometeam['Ball_x']), float(hometeam['Ball_y']), 'ko', markersize=6, alpha=1.0, linewidth=0)
    return fig,ax

  
def save_match_clip(hometeam,awayteam, fpath = 'animations/raw_goals', fname='clip_test', figax=None ,frames_per_second=25, team_colors=('b','r'), field_dimen = (105.0,68.0), include_player_velocities=False,annotate = False, PlayerMarkerSize=10, PlayerAlpha=0.7):
    '''
    
    Creates animation for all the Frames of hometeam and awayteam
    
    Credit: This function is slightly modified version from Metrica_Viz.py made available by Friends Of Tracking community
          that works for our dataFrame object
    


    '''
    
    # check that indices match first
    assert  hometeam['Frame'] == awayteam['Frame'], "Home and away should have same frame number"
    # in which case use home team index
    #index = [int(i) for i in hometeam['Frame'].aslist]
    index = range(hometeam.num_rows)
    # Set figure and movie settings
    FFMpegWriter = animation.writers['ffmpeg']
    metadata = dict(title='Tracking Data', artist='Matplotlib', comment='Before after event clip')
    writer = FFMpegWriter(fps=frames_per_second, metadata=metadata)
    fname = fpath + '/' +  fname + '.mp4' # path and filename
    # create football pitch
    if figax is None:
        fig,ax = plot_pitch(field_dimen=field_dimen)
    else:
        fig,ax = figax
    fig.set_tight_layout(True)
    # Generate movie
    print("Generating animation...",end='')
    with writer.saving(fig, fname, 100):
        for i in index:
            figobjs = [] # this is used to collect up all the axis objects so that they can be deleted after each iteration
            for team,color in zip( [hometeam[i],awayteam[i]], team_colors) :
                x_columns = [c for c in team.columns if c[-2:].lower()=='_x' and c.lower()!='ball_x'] # column header for player x positions
                y_columns = [c for c in team.columns if c[-2:].lower()=='_y' and c.lower()!='ball_y'] # column header for player y positions
                objs, = ax.plot( [float(team[column_name]) for column_name in x_columns if not math.isnan(float(team[column_name]))],
                                [float(team[column_name]) for column_name in y_columns if not math.isnan(float(team[column_name]))],
                                color+'o', markersize=PlayerMarkerSize, alpha=PlayerAlpha ) # plot player positions
                figobjs.append(objs)

                if include_player_velocities:
                    vx_columns = ['{}_vx'.format(c[:-2]) for c in x_columns] # column header for player x positions
                    vy_columns = ['{}_vy'.format(c[:-2]) for c in y_columns] # column header for player y positions
                    objs =  ax.quiver( [float(team[column_name]) for column_name in x_columns],[float(team[column_name]) for column_name in y_columns],
                                      [float(team[column_name]) for column_name in vx_columns], [float(team[column_name]) for column_name in vy_columns],
                                      color=color, scale_units='inches', scale=10.,width=0.0015,headlength=5,headwidth=3,alpha=PlayerAlpha)
                    figobjs.append(objs)  
                    if annotate:
                        objs = [ax.text( float(team[x])+0.5, float(team[y])+0.5, x.split('_')[0], fontsize=10, color=color  ) for x,y in zip(x_columns,y_columns) if not ( np.isnan(float(team[x])) or np.isnan(float(team[y])) )]
                        for i in range(len(objs)): figobjs.append(objs[i])       
            
            objs, = ax.plot( float(team['Ball_x']), float(team['Ball_y']), 'ko', markersize=6, alpha=1.0, linewidth=0)
            figobjs.append(objs)

            # include match time at the top
            frame_minute =  int(float(team['Time [s]'])/60.)
            frame_second =  ( float(team['Time [s]'])/60. - frame_minute ) * 60.
            timestring = "{0}:{1:1.2}".format( str(frame_minute), str(frame_second))
            objs = ax.text(-2.5,field_dimen[1]/2.+1., timestring, fontsize=14 )
            figobjs.append(objs)
            writer.grab_frame()
            # Delete all axis objects (other than pitch lines) in preperation for next frame
            for figobj in figobjs:
                figobj.remove()

    print("done")
    plt.clf()
    plt.close(fig)

                
def save_pitch_control_clip(events,hometeam,awayteam,GKnumbers,params, fpath = 'animations/pitch_control', fname='clip_test', figax=None ,frames_per_second=25, team_colors=('b','r'), field_dimen = (105.0,68.0), include_player_velocities=False,annotate = False, PlayerMarkerSize=10, PlayerAlpha=0.7):
    '''
    Creates animation for all the Frames of hometeam and awayteam with pitch control
    
    Note: This function can take some time due to heavy calculations for pitch control 
    
    '''
   
    
    # check that indices match first
    assert  hometeam['Frame'] == awayteam['Frame'], "Home and away should have same frame number"
    # in which case use home team index
    #index = [int(i) for i in hometeam['Frame'].aslist]
    index = range(hometeam.num_rows)
    # Set figure and movie settings
    FFMpegWriter = animation.writers['ffmpeg']
    metadata = dict(title='Tracking Data', artist='Matplotlib', comment='Before after event clip')
    writer = FFMpegWriter(fps=frames_per_second, metadata=metadata)
    fname = fpath + '/' +  fname + '.mp4' # path and filename
    # create football pitch
    if figax is None:
        fig,ax = plot_pitch(field_color='white', field_dimen = field_dimen)
    else:
        fig,ax = figax
    fig.set_tight_layout(True)
    
    
    print("Generating animation...",end='')
    with writer.saving(fig, fname, 100):
        for i in index:
            figobjs = [] # this is used to collect up all the axis objects so that they can be deleted after each iteration
            for team,color in zip( [hometeam[i],awayteam[i]], team_colors) :
                x_columns = [c for c in team.columns if c[-2:].lower()=='_x' and c.lower()!='ball_x'] # column header for player x positions
                y_columns = [c for c in team.columns if c[-2:].lower()=='_y' and c.lower()!='ball_y'] # column header for player y positions
                objs, = ax.plot( [float(team[column_name]) for column_name in x_columns if not math.isnan(float(team[column_name]))],
                                [float(team[column_name]) for column_name in y_columns if not math.isnan(float(team[column_name]))],
                                color+'o', markersize=PlayerMarkerSize, alpha=PlayerAlpha ) # plot player positions
                figobjs.append(objs)

                if include_player_velocities:
                    vx_columns = ['{}_vx'.format(c[:-2]) for c in x_columns] # column header for player x positions
                    vy_columns = ['{}_vy'.format(c[:-2]) for c in y_columns] # column header for player y positions
                    objs =  ax.quiver( [float(team[column_name]) for column_name in x_columns],[float(team[column_name]) for column_name in y_columns],
                                      [float(team[column_name]) for column_name in vx_columns], [float(team[column_name]) for column_name in vy_columns],
                                      color=color, scale_units='inches', scale=10.,width=0.0015,headlength=5,headwidth=3,alpha=PlayerAlpha)
                    figobjs.append(objs)  
                    if annotate:
                        objs = [ax.text( float(team[x])+0.5, float(team[y])+0.5, x.split('_')[0], fontsize=10, color=color  ) for x,y in zip(x_columns,y_columns) if not ( np.isnan(float(team[x])) or np.isnan(float(team[y])) )]
                        for j in range(len(objs)): figobjs.append(objs[j])
                        
            pass_frame = int(hometeam[i]['Frame'])
            if events[events['Start Frame'] <= pass_frame][len(events['Start Frame'] <= pass_frame)-1]['Team'] == 'Home':
                cmap = 'bwr_r'
            else:
                cmap = 'bwr'
            PPCF,x,y = generate_pitch_control_for_frame(events = events, tracking_home = hometeam[i], tracking_away = awayteam[i], params = params, GK_numbers = GKnumbers)
            img = ax.imshow(np.flipud(PPCF), extent=(-field_dimen[0]/2., field_dimen[0]/2., -field_dimen[1]/2., field_dimen[1]/2.),interpolation='spline36',vmin=0.0,vmax=1.0,cmap=cmap,alpha=0.5)
            figobjs.append(img)
                
            objs, = ax.plot( float(team['Ball_x']), float(team['Ball_y']), 'ko', markersize=6, alpha=1.0, linewidth=0)
            figobjs.append(objs)

            # include match time at the top
            frame_minute =  int(float(team['Time [s]'])/60.)
            frame_second =  ( float(team['Time [s]'])/60. - frame_minute ) * 60.
            timestring = "{0}:{1:1.2}".format( str(frame_minute), str(frame_second))
            objs = ax.text(-2.5,field_dimen[1]/2.+1., timestring, fontsize=14 )
            figobjs.append(objs)
            writer.grab_frame()
            # Delete all axis objects (other than pitch lines) in preperation for next frame
            for figobj in figobjs:
                figobj.remove()

    print("done")
    plt.clf()
    plt.close(fig)                


def plot_events( events, figax=None, field_dimen = (105.0,68.0), indicators = ['Marker','Arrow'], color='r', marker_style = 'o', alpha = 0.5, annotate=False):

    ''''
    Plots events for given row or rows of given events data as a dataFrame
    
    Credit: this function is slightly modified version from metrica_visualize.py made available by Friends Of Tracking community
          that works for our dataFrame object
    '''  



    if figax is None: # create new pitch 
        fig,ax = plot_pitch( field_dimen = field_dimen )
    else: # overlay on a previously generated pitch
        fig,ax = figax 
    for i in range(events.num_rows):
        row = events[i]
        if 'Marker' in indicators:
            
            #First converts to metric coordinates and then plots
            ax.plot(  (float(row['Start X'])-0.5)*field_dimen[0], -(float(row['Start Y'])-0.5)*field_dimen[1], color+marker_style, alpha=alpha )
        if 'Arrow' in indicators:
            ax.annotate("", xy=((float(row['End X'])-0.5)*field_dimen[0],-(float(row['End Y'])-0.5)*field_dimen[1]),xytext=((float(row['Start X'])-0.5)*field_dimen[0], -(float(row['Start Y'])-0.5)*field_dimen[1]),alpha=alpha, arrowprops=dict(arrowstyle="->",alpha=alpha,color=color),annotation_clip=False)
        if annotate:
            textstring = row['Type'] + ': ' + row['From']
            ax.text( (float(row['Start X'])-0.5)*field_dimen[0], -(float(row['Start Y'])-0.5)*field_dimen[1], textstring, fontsize=10, color=color)
    return fig,ax



def plot_pitchcontrol_for_event( event_id, events,  tracking_home, tracking_away, PPCF, alpha = 0.7, include_player_velocities=True, annotate=False, field_dimen = (105.0,68)):
    ''' 
    Plots events with pitch control for given event id
    Note: event id is the row number for the given events dataFrame
    
    Credit: this function is slightly modified version from metrica_visualize.py made available by Friends Of Tracking community
          that works for our dataFrame object

    '''    

    # pick a pass at which to generate the pitch control surface
    pass_frame = int(events[event_id]['Start Frame'])
    pass_team = events[event_id]['Team']
    
    # plot frame and event
    fig,ax = plot_pitch(field_color='white', field_dimen = field_dimen)
    plot_frame( tracking_home[pass_frame], tracking_away[pass_frame], figax=(fig,ax), PlayerAlpha=alpha, include_player_velocities=include_player_velocities, annotate=annotate )
    plot_events( events[event_id], figax = (fig,ax), indicators = ['Marker','Arrow'], annotate=False, color= 'k', alpha=1 )
    
    # plot pitch control surface
    if pass_team=='Home':
        cmap = 'bwr_r'
    else:
        cmap = 'bwr'
    ax.imshow(np.flipud(PPCF), extent=(-field_dimen[0]/2., field_dimen[0]/2., -field_dimen[1]/2., field_dimen[1]/2.),interpolation='spline36',vmin=0.0,vmax=1.0,cmap=cmap,alpha=0.5)

    return fig,ax

    
