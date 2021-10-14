import pygame
import sys
import grid

pygame.init()

size = width,height = 1280,720
grid_size = gwidth,gheight = 50,50

black       = 0  , 0  , 0
white       = 255, 255, 255
enter_color = 0  , 255, 0
exit_color  = 255, 0  , 0
s_color     = 255, 100, 100
p_color     = 255, 0  , 255

screen = pygame.display.set_mode(size)


def step():
    pass

def draw():
    screen.fill(white)
    pygame.display.flip()


def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        step()
        draw()

if __name__ == "__main__":
    main()


