import pygame
import random 
from grid import Grid
from pygame.locals import *
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
SQUARE = 100

# This sets the margin between each cell
MARGIN = 2
 
def create_window(w, h):
    # Set the HEIGHT and WIDTH of the screen
    screen = pygame.display.set_mode([w,h])
    # Set title of screen
    pygame.display.set_caption("John Conway's game of life")
    return screen

# Initialize pygame
pygame.init()

#create window
w = 500
h = 500
screen = create_window(w, h)

# Loop until the user clicks the close button.
done = False
    
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#calculate row_num, col_num from current resolution
row_num = w//SQUARE
col_num = h//SQUARE
#create grid
grid = Grid(row_num, col_num)
print(grid.shape())
#grid.randomize()
grid[1][2] = 1
grid[2][2] = 1
grid[3][2] = 1

#def initialize grid
def draw_grid(row_num, col_num, g):
                # Draw the grid
                for row in range(row_num):
                    for column in range(col_num):
                        color = WHITE
                        pygame.draw.rect(screen,
                                            color,
                                            [(MARGIN + SQUARE) * row + MARGIN,
                                            (MARGIN + SQUARE) * column + MARGIN,
                                            SQUARE,
                                            SQUARE])
                        if g[row][column] == 1:
                            pygame.draw.rect(screen,
                                    GREEN,
                                    [(MARGIN + SQUARE) * row + MARGIN,
                                    (MARGIN + SQUARE) * column + MARGIN,
                                    SQUARE,
                                    SQUARE])
                pygame.display.flip()
                
                        
                    
#draw initial grid
draw_grid(row_num, col_num, grid)                        

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        #elif event.type == pygame.VIDEORESIZE: 
        #    screen=pygame.display.set_mode(event.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
        #    h,w = event.dict['size']
            #screen.blit(pygame.transform.scale(pic,event.dict['size']),(0,0))
        #    pygame.display.flip()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                print('space key pressed')
                x = 0
                while True:
                    next_grid = Grid(row_num, col_num)
                    for row in range(row_num):
                        for col in range(col_num):

                            state = grid[row][col]#current grid state 0 or 1
                            
                             
                            # #ignore edges for the moment --> Already fixed in version 0.8
                            # if row == 0 or row == row_num-1 or col == 0 or col == col_num-1:
                            #     next_grid[row][col] = state
                            #     continue
                            
                            neighbors = grid.alive_neighbors(row,col)#current grid alive neighbors
                            
                            
                            if state == 1 and (neighbors<2 or neighbors>3):
                                next_grid[row][col] = 0
                            elif state == 0 and neighbors == 3: 
                                next_grid[row][col] = 1
                            else:
                                next_grid[row][col] = state
                                
                    draw_grid(row_num, col_num, next_grid)
                    grid = next_grid
                    x+=1
                    print('generation:',x)
                    # Limit to x frames per second
                    clock.tick(1)
                
    

    # Go ahead and update the screen with what we've drawn.
    #pygame.display.update()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()