# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:03:51 2022

@author: hp
"""
import csv
import numpy as np
import visualize
import matplotlib.pyplot as plt
from Player import player
import matplotlib.colors as mcolors
from Edge import edge
import data_structure
        
class graph():
    
    
    def __init__(self):
        self._players_home=[]
        self._edges_home=[]
        self.number_home=11
        self._players_away=[]
        self._edges_away=[]
        self.number_away=11
        self.undirected_home()
        self.createPlayers_home()
        self.createEdges_home()
        self.undirected_away()
        self.createPlayers_away()
        self.createEdges_away()
        
    def undirected_home(self):
        import csv
        rows=[]
        reader = csv.reader(open('passes_home.csv'))
        for row in reader:
                rows.append(row)
        for i in range(11):
            rows[i] = [int(i) for i in rows[i]]
        for i in range(11):
            for j in range(11):
                if (i==j):
                    continue
                if (i<j):
                    rows[i][j]=int(rows[i][j])+int(rows[j][i])
                if(j>i):
                    rows[i][j]=0
        
        d2=data_structure.dataFrame(rows)
        data_structure.dataFrame.save_as_csv(d2,"passesundirected_home.csv")
    def undirected_away(self):
        import csv
        rows=[]
        reader = csv.reader(open('passes_away.csv'))
        for row in reader:
                rows.append(row)
        
        for i in range(11):
            
            rows[i] = [int(i) for i in rows[i]]
        for i in range(11):
            for j in range(11):
                if (i==j):
                    continue
                if (i<j):
                    rows[i][j]=int(rows[i][j])+int(rows[j][i])
                if(j>i):
                    rows[i][j]=0
        
        d2=data_structure.dataFrame(rows)
        data_structure.dataFrame.save_as_csv(d2,"passesundirected_away.csv")
    def createPlayers_home(self):
        file = open("avg1_home.csv")
        csvreader=csv.reader(file)
        for row in csvreader:
            p=player()
            p._x=float(row[0])
            p._y=float(row[1])
            p._num=int(row[2])
            self._players_home.append(p)
    
    def renderPlayers_num_home(self):
        listofnum=[]
        for i in range(11):
            listofnum.append(self._players_home[i].get_num())
        return(listofnum)
    def createPlayers_away(self):
        file = open("avg1_away.csv")
        csvreader=csv.reader(file)
        for row in csvreader:
            p=player()
            p._x=float(row[0])
            p._y=float(row[1])
            p._num=int(row[2])
            self._players_away.append(p)
    
    def renderPlayers_num_away(self):
        listofnum=[]
        for i in range(11):
            listofnum.append(self._players_away[i].get_num())
        return(listofnum)
    def renderPlayers_x_home(self):
        listofx=[]
        
        for i in range(11):
            listofx.append(self._players_home[i].get_x())
            
        return(listofx)
    def renderPlayers_x_away(self):
        listofx=[]
        
        for i in range(11):
            listofx.append(self._players_away[i].get_x())
            
        return(listofx)
    def renderPlayers_y_home(self):
        
        listofy=[]
        for i in range(11):
            
            listofy.append(self._players_home[i].get_y())
        return(listofy)
    def renderPlayers_y_away(self):
        
        listofy=[]
        for i in range(11):
            
            listofy.append(self._players_away[i].get_y())
        return(listofy)

            
    def createEdges_home(self):
        file = open("passesundirected_home.csv")
        csvreader=csv.reader(file)
        i=0
        for row in csvreader:
            j=0
            for element in row:
                if(element!=0):
                    e=edge(self._players_home[i],self._players_home[j],element)
                    self._edges_home.append(e)
                j=j+1
            i=i+1
    def createEdges_away(self):
        file = open("passesundirected_away.csv")
        csvreader=csv.reader(file)
        i=0
        for row in csvreader:
            j=0
            for element in row:
                if(element!=0):
                    e=edge(self._players_away[i],self._players_away[j],element)
                    self._edges_away.append(e)
                j=j+1
            i=i+1
    def draw(self,point1,point2,volume):
        # point1 = [10, 20]
        # point2 = [30, 40]
        col ={"1":"#F89682","2":"#F59581","3":"#E48C7A","4":"#D0725F","5":"#C44D3C","6":"#BC4B3B","7":"#B24738","8":"#A04235","9":"#933E32","10":"#80372D","11":"#703129","12":"#57251E","13":"#4B201A"}
        
        if int(volume)>0:
            string=col[volume]
            x_values = [point1[0], point2[0]]
            y_values = [point1[1], point2[1]]
            
            plt.plot(x_values, y_values,  linestyle="-",color=string)
        # plt.text(point1[0]-0.015, point1[1]+0.25, "Point1")
        # plt.text(point2[0]-0.050, point2[1]-0.25, "Point2")

    def renderEdges_home(self):
        for e in self._edges_home:
            x1=e.get_from().get_x()
            x2=e.get_to().get_x()
            y1=e.get_from().get_y()
            y2=e.get_to().get_y()
            vol=e.get_volume()
            self.draw((x1,y1),(x2,y2),vol)
            
    def renderEdges_away(self):
        for e in self._edges_away:
            x1=e.get_from().get_x()
            x2=e.get_to().get_x()
            y1=e.get_from().get_y()
            y2=e.get_to().get_y()
            vol=e.get_volume()
            self.draw((x1,y1),(x2,y2),vol)
    def plot_graph_home(self, field_dimen = (105.0,68.0), field_color ='green', linewidth=2, markersize=15):
        
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
        posx=g.renderPlayers_x_home()
        posy=g.renderPlayers_y_home()
        num=g.renderPlayers_num_home()
        
        plt.scatter(posx,posy,marker='o',s=270)
        g.renderEdges_home()
        
        for i in range (11):
            xatpoint=posx[i]-0.7
            yatpoint=posy[i]-0.7
            numatpoint=num[i]
            #plt.plot(xatpoint,yatpoint,marker='o',s=150)
            strings=str(numatpoint)
            plt.annotate(strings,(xatpoint,yatpoint),color='black')
        
        # plt.plot(int(posx[4]),int(posy[4]),'ro')
        plt.show()
    def plot_graph_away(self, field_dimen = (105.0,68.0), field_color ='green', linewidth=2, markersize=15):
        
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
        
        posx=g.renderPlayers_x_away()
        posy=g.renderPlayers_y_away()
        num=g.renderPlayers_num_away()
        
        plt.scatter(posx,posy,marker='o',s=270)
        g.renderEdges_away()
        
        for i in range (11):
            xatpoint=posx[i]-0.7
            yatpoint=posy[i]-0.7
            numatpoint=num[i]
            #plt.plot(xatpoint,yatpoint,marker='o',s=150)
            strings=str(numatpoint)
            plt.annotate(strings,(xatpoint,yatpoint),color='black')
        
        # plt.plot(int(posx[4]),int(posy[4]),'ro')
        plt.show()
        

    
if __name__=='__main__':
    g=graph()
        
    g.plot_graph_home()
    g.plot_graph_away()

    


    
    

