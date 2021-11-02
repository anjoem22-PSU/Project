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
        
    def step(self,grid):
        pass