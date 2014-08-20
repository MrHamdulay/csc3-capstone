"""Mphuthi Mamorena
assignment 7
question2
29 April 2014"""

# creating 4 x 4 grid
def create_grid(grid):
        for i in range(4):
                grid.append([0]*4)
        return grid


# printing the grid
def print_grid(grid):
        print('+','-'*20,'+',sep='')#printing the top frame 
        for i in range (4):
                print('|',end='')
                for f in range(4):
                        if grid[i][f]==0:
                                print(' ',' '*(4-len(str(grid[i][f]))),end='')#printing a blank if the value is 0 
                        else:
                                print(grid[i][f],' '*(4-len(str(grid[i][f]))),end='')# printing each value in a grid
                print('|')
        print('+','-'*20,'+',sep='')#printing the bottom frame 
    


    
def check_lost(grid):
        for row in range(4):
                for col in range(4):
                        if grid[row][col]==0:# checking if there are zeros in every row meaning spaces and returning false
                                return False
        for row in range(4):
                for col in range(4): 
                        position=grid[row][col] #accessing every position in a grid
                        if 0<=col+1<4:
                                if position==grid[row][col+1]:#checking for adjecent numbers after a position horizontaly
                                        return False
                        if 0<=col-1<4:
                                if position==grid[row][col-1]:#checking for adjecent numbers before a position horizontaly
                                        return False
                        if 0<=row+1<4:
                                if position==grid[row+1][col]:#checking for adjecent numbers under vertically
                                        return False   
                        if 0<row-1<4:
                                if position==grid[row-1][col]:#checking for adjecent numbers on top vertically
                                        return False                        
                        
        return True
                                


def check_won(grid):
        won = False
        for i in range(4):
                for f in range(4):
                        if grid[i][f]>=32:#cheicking for number equal or greater than 32
                                won =True 
        return won
                      
def copy_grid(grid):
        newgrid = []  
        for i in range(4):
                newgrid.append([0]*4)        
        for i in range(4):
                for j in range(4):
                        newgrid[i][j]=grid[i][j]#making a copy of a grid by replacing values in newgrid by values in the grid
        return newgrid
 
def grid_equal(grid1,grid2):
        if grid1==grid2:# checking if grids are equal
                return True
        else:
                return False

        

                                