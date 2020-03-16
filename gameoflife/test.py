from grid import Grid

grid = Grid(5,5)
grid.randomize()


grid2 = Grid(5,5)
grid2.to_tuple()
if __name__ == '__main__':
    print('grid:',grid)
    print('grid to tuple:',grid.to_tuple())
    print('set of grid:',set(grid))
    #pprint(grid2)
    #print(set(grid2)&set(grid))