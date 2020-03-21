import random

class Grid(list):
    def __init__(self, w, h):
        """
        initializes a grid of zeros with weight w and height h containing 
        """
        self.w = w
        self.h = h
        super()
        for row in range(w):
        # Add an empty array that will hold each cell
        # in this row
            self.append([])
            for column in range(h):
                self[row].append(0)  # Append a cell
    
    def show(self):
        for row in range(self.w):
            ch='['
            for col in range(self.h):
                ch += str(self[row][col])+','
            if col == self.h-1:
                ch=ch[:-1]+']'
                print(ch,'\n')

    def sum(self):
        res = 0
        for row in range(self.w):
            res+= sum(self[row])
        return res


    def shape(self):
        """
        returns the shape of the grid
        """
        return self.w,self.h

    def randomize(self):
        """
        Sets the grid to random 1's and 0's
        """
        for row in range(self.w):
            for col in range(self.h):
                    self[row][col] = random.randint(0,1)

    def alive_neighbors(self,x,y):
        """
        returns the number of alive neighbors (=1) for a certain x,y position
        """
        res = 0
        for row in range(x-1,x+2):
            for col in range(y-1,y+2):
                if (row==x) and (col==y):
                    continue
                try:
                    if self[row][col] == 1:
                        res+=1
                        pass
                except IndexError:#If this error is raised for cells on the edges we consider the next edge cells are the neighbors, like we are wrapping a sheet of paper so the edges touch 
                    row = (x+row+self.w)%self.w
                    col = (y+col+self.h)%self.h
                        
        return res

    def to_tuple(self):
        """
        Convert the nested list into a list of tuples so to be able to compare grids for test puposes
        """
        for row in range(self.w):
            self[row] = tuple(self[row])
        return self
















