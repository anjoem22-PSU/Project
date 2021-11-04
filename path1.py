class Pathfinder():
    def __init__(self,start_point,end_point,grid_width,grid_height):
        self.width = grid_width
        self.height = grid_height
        
        self.stage = 0
        
        self.start = start_point
        self.end = end_point
        
        self.distances = []
        self.visited_grid = []
        self.to_visit = [start_point]
        
        self.final_path = [end_point]
        
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
        if grid[pos[1]][pos[0]] == 1:
            return False
        if self.visited_grid[pos[1]][pos[0]] == True:
            return False
        return True
    
    def attempt_additions(self,pos,current_dist,grid):
        if not self.position_available(pos,grid):
            return
        
        new_dist = current_dist + 1
        if self.distances[pos[1]][pos[0]] == -1 or self.distances[pos[1]][pos[0]] > new_dist:
            self.distances[pos[1]][pos[0]] = new_dist
            self.to_visit.append(pos)
        
        if pos[0] == self.end[0] and pos[1] == self.end[1]:
            self.stage = 1
    
    def build_path(self,positions):
        append_pos = None
        for pos in positions:
            if pos[0] < 0 or pos[0] >= self.width:
                continue
            if pos[1] < 0 or pos[1] >= self.height:
                continue
            if pos[0] == self.start[0] and pos[1] == self.start[1]:
                self.final_path.append(pos)
                return True
            if not append_pos or self.distances[pos[1]][pos[0]] > self.distances[append_pos[1]][append_pos[1]]:
                append_pos = pos
                
        self.final_path.append(append_pos)
        return False
    
    def step(self,grid):
        if self.stage == 0:
            if len(self.to_visit) == 0:
                return True
            
            current_pos = self.to_visit.pop(0)
            current_dist = self.distances[current_pos[1]][current_pos[0]]
            
            up =    [current_pos[0],current_pos[1] + 1]
            down =  [current_pos[0],current_pos[1] - 1]
            right = [current_pos[0] + 1,current_pos[1]]
            left =  [current_pos[0] - 1,current_pos[1]]
            
            self.attempt_additions(up,current_dist,grid)
            self.attempt_additions(down,current_dist,grid)
            self.attempt_additions(right,current_dist,grid)
            self.attempt_additions(left,current_dist,grid)
            
            self.visited_grid[current_pos[1]][current_pos[0]] = True
            
            return False
        else:
            current_pos = self.final_path[-1]
            
            up =    [current_pos[0],current_pos[1] + 1]
            down =  [current_pos[0],current_pos[1] - 1]
            right = [current_pos[0] + 1,current_pos[1]]
            left =  [current_pos[0] - 1,current_pos[1]]
            
            success = self.build_path((up,down,left,right))
            
            if success:
                return True
            else:
                return False
