import pygame
import random 
from grid import Grid
from pygame.locals import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
SQUARE_WIDTH = 20
SQUARE_HEIGHT = 20

# This sets the margin between each cell
MARGIN = 2
 
def create_window(w, h):
    # Set the HEIGHT and WIDTH of the screen
    screen = pygame.display.set_mode([w,h], HWSURFACE|DOUBLEBUF|RESIZABLE)
    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")
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
row_num = (w//SQUARE_WIDTH+MARGIN)
col_num = (h//SQUARE_HEIGHT+MARGIN)
#create grid
grid = Grid(row_num, col_num)
grid.randomize()

#def initialize grid
def draw_grid(row_num, col_num):
                # Draw the grid
                for row in range(row_num):
                    for column in range(col_num):
                        color = WHITE
                        pygame.draw.rect(screen,
                                            color,
                                            [(MARGIN + SQUARE_WIDTH) * row + MARGIN,
                                            (MARGIN + SQUARE_HEIGHT) * column + MARGIN,
                                            SQUARE_WIDTH,
                                            SQUARE_HEIGHT])
                for row in range(row_num):
                    for column in range(col_num):
                        if grid[row][column] == 1:
                            pygame.draw.rect(screen,
                                    GREEN,
                                    [(MARGIN + SQUARE_WIDTH) * row + MARGIN,
                                    (MARGIN + SQUARE_HEIGHT) * column + MARGIN,
                                    SQUARE_WIDTH,
                                    SQUARE_HEIGHT])
                    
#draw initial grid
draw_grid(row_num, col_num)                        

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
                test_grid = tuple(grid)
                print(type(test_grid))
                test_grid = set(test_grid)
                print(type(test_grid))
                
                #while True:
                for row in range(1,row_num-1):
                    for col in range(1,col_num-1):
                        if ((grid.alive_neghibors(row,col)<2) or (grid.alive_neghibors(row,col)>3)) and (grid[row][col] == 1):
                            grid[row][col] = 0
                        if (grid.alive_neghibors(row,col) == 3) and (grid[row][col] == 0):
                            grid[row][col] == 1
                print(f'Num of elements: {(row_num-1)*(col_num-1)} \n ',set(grid)&set(test_grid))
                draw_grid(row_num, col_num)
                pygame.display.update()
                x+=1
                # Limit to x frames per second
                clock.tick(x)
                print('pass:',x)
    

    # Go ahead and update the screen with what we've drawn.
    #pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()