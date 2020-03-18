from grid import Grid
import time

grid = Grid(5,5)

grid[1][1] = 1
grid[1][2] = 1
grid[1][3] = 1



if __name__ == '__main__':
    print(grid.alive_neighbors(1,3))
    grid.show()
    next_grid = Grid(5,5)
    x=0
    while x<2:
        for row in range(5):
            for col in range(5):
                
                state = grid[row][col]
                #get every element's neighbors of grid
                neighbors = grid.alive_neighbors(row,col)

                if neighbors == 3 and state ==0 :
                    next_grid[row][col] = 1
                elif (neighbors<2 or neighbors>3) and state ==1 :
                    next_grid[row][col] = 0
                else:
                    next_grid[row][col] = state
        x+=1
        print('='*10)
        next_grid.show()        
        grid = next_grid


    
    
                           
                