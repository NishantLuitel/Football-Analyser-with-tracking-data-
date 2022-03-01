class player:
    
    def __init__(self,x=0,y=0,num=0):
        self._x=x
        self._y=y
        self._num =num
        # self._edges=set()
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    def get_player(self):
        return self 
    def __str__(self):
        return "x = "+self._x+" y = "+self._y+" num = "+self._num
    # def add_edge(self,edges):
    #     self._edges.add(edges)
    
        
    
        
    # def get_edges(self):
    #     return self._edges

    def get_num(self):
        return self._num
    
    # def remove_edge(self,edge):
    #     if edge in self._edges:
    #         self._edges.remove(edge)
    #     else:
    #         raise ValueError("error")