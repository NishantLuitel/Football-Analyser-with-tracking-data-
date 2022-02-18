from Player import player
class edge():
    
    def __init__(self,fro=0,to=0,volume=0):
        self._volume=volume
        self._from=fro
        self._to=to
        #player.__init__(self,fro,to)
    
    def get_from(self):
        return self._from
    def get_to(self):
        return self._to
    def get_volume(self):
        return self._volume
    
    def __str__(self):
        return "from player no "+str(self._from._num)+" to player no  "+str(self._to._num)+" volume is  "+str(self._volume)