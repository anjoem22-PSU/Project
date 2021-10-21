class Pathfinder():
    def __init__(self,start_point,end_point,grid_width,grid_height):
        self.width = grid_width
        self.height = grid_height
        
        self.start = start_point
        self.end = end_point
        
        self.opened = []
        self.closed = []
        
    def step(self,grid):
        pass