# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:03:51 2022

@author: hp
"""
from Player import player
from Edge import edge
        
class graph():
    
    
    def __init__(self):
        self.__players={}
        self.__edges=set()
        
        # self.player1=player1;
        # self.player2=player2;
        # self.edge1=edge1;
    def addedge(self,fro,to,volume):
        self.volume=volume
        self.fro=fro
        self.to=to    
    # def addedge(self,player1,player2,vol)
    
    def plot(self):
        print("the pass came between player {} and player {} is {} ".format(self.player1.num ,self.player2.num,self.edge1.volume))

p1=player(0,0,1)
p2=player(0,0,2)
e1=edge(p1,p2,44)
#e1.defit()
g1=graph(p1,p2,e1)
g1.plot()
g=graph(p1,p2,edge)
p3=player()
p3.addplayer(0,0,3)
p3.getdetail()
e2=edge()
e2.addedge(p1,p3,33)
e2.display()

# graph g(p1,p2,e1)
# g.plot

        