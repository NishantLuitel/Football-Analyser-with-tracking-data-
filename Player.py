class player:
    
    def __init__(self,x=0,y=0,num=0):
        self.x=x
        self.y=y
        self.num =num
        self.edges=set()
    
    def getdetail(self):
        print("the player is {}".format(self.num))
        
    def addplayer(self,x=0,y=0,num=0):
        self.x=x
        self.y=y
        self.num=num
        
    def get_edges(self):
        return self.edges

    def get_num(self):
        return self.num
    
    def remove_edge(self,edge):
        if edge in self.edges:
            self.edges.remove(edge)
        else:
            raise ValueError("error")