from Player import player
import matplotlib.pyplot as plt
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
    
    # def draw(self):
    #     point1 = [10, 20]
    #     point2 = [30, 40]
    #     x_values = [point1[0], point2[0]]
    #     y_values = [point1[1], point2[1]]
    #     plt.plot(x_values, y_values, 'bo', linestyle="--")
        # plt.text(point1[0]-0.015, point1[1]+0.25, "Point1")
        # plt.text(point2[0]-0.050, point2[1]-0.25, "Point2")

