# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:03:51 2022

@author: hp
"""

class player:
    
    def __init__(self,x,y,num):
        self.x=x
        self.y=y
        self.num =num
    
    def getdetail(self):
        print("the player is {}".format(self.num))
    

class edge(player):
    
    def __init__(self,fro,to,volume):
        self.volume=volume
        
        self.fro=fro
        self.to=to
        #player.__init__(self,fro,to)
    def addegdge(self,fro,to,volume):
        pass
        
    
    # def defit(self):
    #     print("the edge is from {} to {}".format(self.fro.num,self.to.num))
        
        
class graph(edge,player):
    
    
    def __init__(self,player1,player2,edge1):
        self.player1=player1;
        self.player2=player2;
        self.edge1=edge1;
    
    # def addedge(self,player1,player2,vol)
    
    def plot(self):
        print("the pass came between player {} and player {} is {} ".format(self.player1.num ,self.player2.num,self.edge1.volume))

p1=player(0,0,1)
p2=player(0,0,2)
e1=edge(p1,p2,4)
#e1.defit()
g1=graph(p1,p2,e1)
g1.plot()
g=graph(p1,p2,edge)

# graph g(p1,p2,e1)
# g.plot

        