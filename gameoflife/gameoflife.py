import pygame
import random 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Window Height
WINDOW_HEIGHT = 500
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
rectangle_number = WINDOW_HEIGHT//WIDTH #number of rectangles in window aka grig
grid = []
for row in range(rectangle_number):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(rectangle_number):
        grid[row].append(0)  # Append a cell

#initializz random cells in grid 
print(len(grid))
for row in range(rectangle_number):
    for col in range(rectangle_number):
        if row == random.randint(1,rectangle_number) or col == random.randint(1,rectangle_number):
            grid[row][col] = 1
print(grid)
# This sets the margin between each cell
MARGIN = 2
 
# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [WINDOW_HEIGHT, WINDOW_HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Set the screen background
screen.fill(BLACK)

# Draw the grid
for row in range(rectangle_number):
    for column in range(rectangle_number):
        color = WHITE
        pygame.draw.rect(screen,
                            color,
                            [(MARGIN + WIDTH) * column + MARGIN,
                            (MARGIN + HEIGHT) * row + MARGIN,
                            WIDTH,
                            HEIGHT]) 
        if grid[row][column] == 1:
            pygame.draw.rect(screen,
                    GREEN,
                    [(MARGIN + WIDTH) * row + MARGIN,
                    (MARGIN + HEIGHT) * column + MARGIN,
                    WIDTH,
                    HEIGHT])

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        #elif 
 
    
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()