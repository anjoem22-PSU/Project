# 0 = empty, 1 = wall, 2 = begin, 3 = end, 4 = searched, 5 = path
def Grid():
    def __init__(self,width,height,data = None):
        self.width = width
        self.height = height
        
        if data:
            self.values = data
        else:
            self.values = [ [0]*width for _ in range(height) ]
    
    
    def reset():
        for y,row in enumerate(self.values):
            for x,val in y:
                if val > 3:
                    self.values[y][x] = 0
                        
