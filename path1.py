class Pathfinder():
    def __init__(self,start_point,end_point,grid_width,grid_height):
        self.width = grid_width
        self.height = grid_height
        
        self.start = start_point
        self.end = end_point
        
        self.distances = []
        self.visited_grid = []
        self.to_visit = [start_point]
        
        for y in range(grid_height):
            self.distances.append([])
            for x in range(grid_width):
                self.distances[y].append(-1)
        
        for y in range(grid_height):
            self.visited_grid.append([])
            for x in range(grid_width):
                self.visited_grid[y].append(False)
        
        self.distances[start_point[1]][start_point[0]] = 0
    
    def position_available(self,pos,grid):
        if pos[0] < 0 or pos[0] >= self.width:
            return False
        if pos[1] < 0 or pos[1] >= self.height:
            return False
        if grid[pos[1]][pos[0]] == 0:
            return False
        return True
    
    def attempt_additions(self,pos,current_dist,grid):
        pass
    
    def step(self,grid):
        if len(self.to_visit) == 0:
            return True
        
        current_pos = self.to_visit.pop(0)
        current_dist = self.distances[current_pos[1]][current_pos[0]]
        
        up =    [current_pos[0],current_pos[1] + 1]
        down =  [current_pos[0],current_pos[1] - 1]
        right = [current_pos[0] + 1,current_pos[1]]
        left =  [current_pos[0] - 1,current_pos[1]]
        
        attempt_addition(self,up,current_dist,grid)
        attempt_addition(self,down,current_dist,grid)
        attempt_addition(self,right,current_dist,grid)
        attempt_addition(self,left,current_dist,grid)
        
        return False