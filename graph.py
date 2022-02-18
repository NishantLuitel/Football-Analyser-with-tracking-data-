# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 14:03:51 2022

@author: hp
"""
import csv
from tkinter import E
from Player import player
from Edge import edge
        
class graph():
    
    
    def __init__(self):
        self._players=[]
        self._edges=[]
        self.number=11
    
    def createPlayers(self):
        file = open("data1.csv")
        csvreader=csv.reader(file)
        for row in csvreader:
            p=player()
            p._x=row[0]
            p._y=row[1]
            p._num=row[2]
            self._players.append(p)
        
    def createEdges(self):
        file = open("data2.csv")
        csvreader=csv.reader(file)
        i=0
        for row in csvreader:
            j=0
            for element in row:
                if(element!=0):
                    e=edge(self._players[i],self._players[j],element)
                    self._edges.append(e)
                j=j+1
            i=i+1
                                
        for i in self._edges:
            print(i)        
        
        # print(self._players)
        #     #reading data from the file for each player

g=graph()
g.createPlayers()
g.createEdges()

#     # def get_player(self,x=0,y=0,num=0):
#     #     return self._edges
        
#     # def add_player(self,x,y,num):
#     #     if num not in self._players:
#     #         self._players[num]=player(x,y,num)
#     #     # self.player1=player1;
#     #     # self.player2=player2;
#     #     # self.edge1=edge1;
#     # def add_edge(self,start_player,to_player,volume=0):
#     #     fro=self.get_player(start_player)
#     #     to= self.get_player(to_player)
#     #     Edg=edge(fro,to,volume)
#     #     fro.add_edge(edg)
#     #     self._edges.add(edge)
        
#     # def addedge(self,player1,player2,vol)
    
#     def plot(self):
#         print("the pass came between player {} and player {} is {} ".format(self.player1.num ,self.player2.num,self.edge1.volume))

# p1=player(0,0,1)
# p2=player(0,0,2)
# e1=edge(p1,p2,44)
# #e1.defit()
# g1=graph(p1,p2,e1)
# g1.plot()
# g=graph(p1,p2,edge)
# p3=player()
# p3.addplayer(0,0,3)
# p3.getdetail()
# e2=edge()
# e2.addedge(p1,p3,33)
# e2.display()

# graph g(p1,p2,e1)
# g.plot

        