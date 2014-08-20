"""Module containing functions capable of manipulating 2D arrays of size 4X4
Pankaj Munbodh
28 April 2014"""

def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])
    return grid

def print_grid(grid):
    print("+"+"-"*20+"+")

    for j in range(4):
        print("|",end='')
        for i in range(4):
            if i!=3:
                if grid[j][i]==0:
                    print(" "*5,end='')
                else :
                    print("{0:<5}".format(grid[j][i]),end='')
            else:
                if grid[j][i]==0:
                    print(" "*5+"|")
                else:
                    print("{0:<5}".format(grid[j][i])+"|")
                    
    print("+" + "-"*20 + "+")
    
def check_lost (grid):
    for j in range(4):
        for i in range(4):
            if grid[i][j]==0:
                return False
            else:
                if i==0 and j==0:
                    if grid[0][0]==grid[0][1] or grid[0][0]==grid[1][0]:
                        return False
                elif i==0 and j==3:
                    if grid[0][3]==grid[0][2] or grid[0][3]==grid[1][3]:
                        return False
                elif i==0:
                    if grid[0][j]==grid[1][j] or grid[0][j]==grid[0][j+1] or grid[0][j]==grid[0][j-1]:
                        return False
                elif j==0 and i!=3:
                    if grid[i][0]==grid[i][1] or grid[i][0]==grid[i+1][0] or grid[i][0]==grid[i-1][0]:
                        return False
                elif i==3 and j==0:
                    if grid[3][0]==grid[3][1] or grid[3][0]==grid[2][0]:
                        return False                
                
                elif i==3 and j==3:
                    if grid[i][3]==grid[i][2] or grid[i][3]==grid[i-1][3]:
                        return False
                elif i==3 and (j==1 or j==2):
                    if grid[3][j]==grid[2][j] or grid[3][j]==grid[3][j+1] or grid[3][j]==grid[3][j-1]:
                        return False
                elif j==3 and (i==1 or i==2):
                    if grid[i][3]==grid[i][2] or grid[i][3]==grid[i+1][3] or grid[i][3]==grid[i-1][3]:
                        return False
                elif j==1:
                    if grid[i][1]==grid[i][0] or grid[i][1]==grid[i][2] or grid[i][1]==grid[i+1][1] or grid[i][1]==grid[i-1][1]:
                        return False
                elif j==2:
                    if grid[i][2]==grid[i][1] or grid[i][2]==grid[i][3] or grid[i][2]==grid[i+1][2] or grid[i][2]==grid[i-1][2]:
                        return False                    
            
            
                

    return True
    
def check_won (grid):
    for j in range(4):
        for i in range(4):
            if grid[i][j]>=32:
                return True
    else:
        return False
    
def copy_grid (grid):
    grid1=[]
    for i in range(4):
            grid1.append([0,0,0,0])
    for j in range(4):
        for i in range(4):
            grid1[i][j]=grid[i][j]
    return grid1

def grid_equal (grid1, grid2):
    if grid1 == grid2:
        return True
    else :
        return False
    
  