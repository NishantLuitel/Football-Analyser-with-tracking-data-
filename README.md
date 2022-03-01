#   Learn to analyze tracking and events data

 

#Custom dataFrame

data_structure.py consists of our custom dataFrame that mimics to some extent the DataFrame of Pandas library
We have used this custom dataFrame instead of the popular libraries like Pandas and Numpy throughout this project.



#Modules to run

1. Run stats.py for individual stats for the given team
2. Run graph.py for graph visualization of passess between players
3. Run goal_animation.py for creating simple goal animations
4. Run pc_animation.py for creating goal animations integrated with pitch control



Note : This project can be slightly modified to animate pitch control for any event


#Coordinate system of sample data has been changed from Metrica sports coordinate to our metric system 

    #   Y                                                  Y
    #   |                                                  | 
    #   |                                                  |
    #   |(0,0)                        (1,0)                |(-0.5,0.5)                    (0.5,0.5)
    #   ,--------------,--------------,                    ,--------------,--------------,
    #   |              |              |                    |              |              |
    #   |--,           |           ,--|                    |--,           |           ,--|
    #   |  |          <|>(0.5,0.5) |  |         ------>    |  |          <|>(0,0)     |  |
    #   |--'           |           '--|                    |--'           |           '--| 
    #   |              |              |                    |              |              |  
    #   '--------------'--------------'  ------X           '--------------'--------------'------X
    #   (0,1)                         (1,1)                (-0.5,-0.5)                         (0.5,-0.5)
    #
    #    Metrica sports coordinate                                Our metric system
    #    --------------------------                               ----------------------               

        
#File directory Required for this project
    
        │
        ├── animations\
        │   │
        │   ├── pitch_control\
        │   │
        │   └── raw_goals\
        │
        │
        ├── data\
        │   │
        │   ├── Sample_Game_1\
        │   │   │
        │   │   ├── to_metric\
        │   │   │   │
        │   │   │   ├── with_speed\
        │   │   │
        │   │   ├── Sample_Game_1_RawEventsData.csv
        │   │   ├── Sample_Game_1_RawTrackingData_Away_Team.csv
        │   │   └── Sample_Game_1_RawTrackingData_Home_Team.csv
        │   │
        │   ├── Sample_Game_2\
        │       │
        │       ├── to_metric\
        │       │   │
        │       │   ├── with_speed\
        │       │
        │       ├── Sample_Game_2_RawEventsData.csv
        │       ├── Sample_Game_2_RawTrackingData_Away_Team.csv
        │       └── Sample_Game_2_RawTrackingData_Home_Team.csv
        │
        ├── README.md
        ├── calc.py
        ├── data_structure.py
        ├── goal_animation.py
        ├── pc_animation.py
        ├── pitch_control.py
        ├── practice.py
        ├── stats.py
        ├── tracker_utils.py
        ├── graph.py
        ├── visualize.py
        ├── Edge.py
        ├── Player.py

    
    