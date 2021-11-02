import pygame
import sys

import path1 as pf # path1 is placeholder

pygame.init()

size = width,height = 1920,1080
grid_size = gwidth,gheight = 192,108

rect_size = height // gheight
draw_pos = x0,y0 = (width - (rect_size * gwidth)) // 2, (height - (rect_size * gheight)) // 2

black       = 0  , 0  , 0
white       = 255, 255, 255
gray        = 100, 100, 100
enter_color = 0  , 200, 0
exit_color  = 255, 0  , 0
s_color     = 255, 100, 100
p_color     = 255, 0  , 255

screen = pygame.display.set_mode(size)

def pixel_to_grid(pos):  
    x = (pos[0] - x0) // rect_size
    y = (pos[1] - y0) // rect_size
    
    if x < 0:
        x = 0
    if x > gwidth - 1:
        x = gwidth - 1
    if y < 0:
        y = 0
    if y > gheight - 1:
        y = gheight - 1
    
    return (x,y)

def grid_to_pixel(pos):
    x = x0 + rect_size * pos[0]
    y = y0 + rect_size * pos[1]
    return (x,y)

def step(grid,start_pos,end_pos):
    m_pos = pygame.mouse.get_pos()
    m_buttons = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    
    g_pos = pixel_to_grid(m_pos)
    if g_pos:
        if m_buttons[0]:
            grid[g_pos[1]][g_pos[0]] = 1
        elif m_buttons[2]:
            grid[g_pos[1]][g_pos[0]] = 0
            
        if keys[pygame.K_z]:
            if not (g_pos == tuple(end_pos)):
                start_pos[0] = g_pos[0]
                start_pos[1] = g_pos[1]
        elif keys[pygame.K_x]:
            if not (g_pos == tuple(start_pos)):
                end_pos[0] = g_pos[0]
                end_pos[1] = g_pos[1]

def pathfind_step(Path_Tool,grid,start_pos,end_pos):  
    Path_Tool.step(grid)

def draw(grid,start_pos,end_pos,Path_Tool = None):
    screen.fill(gray)
    pygame.draw.rect(screen,white,pygame.Rect(*draw_pos,rect_size * gwidth,rect_size * gheight))
    
    for y,row in enumerate(grid):
        for x,tile in enumerate(row):
            if tile == 1:
                pos = grid_to_pixel((x,y))
                pygame.draw.rect(screen,black,pygame.Rect(*pos,rect_size,rect_size))
    
    start_x,start_y = grid_to_pixel(start_pos)
    pygame.draw.rect(screen,enter_color,pygame.Rect(start_x,start_y,rect_size,rect_size))
    
    end_x,end_y = grid_to_pixel(end_pos)
    pygame.draw.rect(screen,exit_color,pygame.Rect(end_x,end_y,rect_size,rect_size))
    
    pygame.display.flip()


def main():
    start_pos = [0,0]
    end_pos = [gwidth-1,gheight-1]
    
    grid = []
    
    run_mode = 0
    path_started = False
    Path_Tool = None
    
    for y in range(gheight):
        grid.append([])
        for x in range(gwidth):
            grid[y].append(0)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    run_mode = 1
        
        if (run_mode == 0):
            step(grid,start_pos,end_pos)
            draw(grid,start_pos,end_pos)
        else:
            if not path_started:
                Path_Tool = pf.Pathfinder(start_pos,end_pos,gwidth,gheight)
            pathfind_step(Path_Tool,grid,start_pos,end_pos)
            draw(grid,start_pos,end_pos,Path_Tool)
        
        

if __name__ == "__main__":
    main()