from grid import Grid

grid = Grid(5,5)
grid.randomize()

if __name__ == '__main__':
    grid.show()
    print(grid.alive_neghibors(0,0))

                           
                