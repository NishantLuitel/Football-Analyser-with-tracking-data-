from Player import player
class edge():
    
    def __init__(self,fro=0,to=0,volume=0):
        self.volume=volume
        self.fro=fro
        self.to=to
        #player.__init__(self,fro,to)
    
        
    
    def display(self):
        print("the edge is from {} to {}".format(self.fro.num,self.to.num))
        