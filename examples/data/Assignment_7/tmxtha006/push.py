"""This program contains functions to merge adjecent numbers in the grid until 2048 is found
Hebert Tema
28-04-2014"""


import util



def left_add(array):
    """pushes the values in a row while adding"""
    ans=[0,0,0,0]
    index=0
    while array:
        if array[0]==0:
            array.pop(0)
        elif len(array)==1:
            ans[index]=array[0]
            array.pop(0)
        elif array[1]==0:
            array.pop(1)
        elif array[0]==array[1]:
            ans[index]=(array[0])*2
            array.pop(0)
            array.pop(0)
            index+=1
        else:
            ans[index]=array[0]
            array.pop(0)
            index+=1
    return ans

def right_add(array):
    """pushes the values in a row while adding"""
    index=-1
    ans=[0,0,0,0]
    while array:
        if array[-1]==0:
            array.pop(-1)
        elif len(array)==1:
            ans[index]=array[-1]
            array.pop(-1)
        elif array[-2]==0:
            array.pop(-2)
        elif array[-1]==array[-2]:
            ans[index]=(array[-1])*2
            array.pop(-1)
            array.pop(-1)
            index-=1
        else:
            ans[index]=array[-1]
            array.pop(-1)
            index-=1
    return ans

def push_down(grid):
    """merge grid values upwards"""
    grid2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    counter=-1
    while counter>-5:
        i=[]
        for j in grid:
            i.append(j[counter])
        ans=right_add(i)
        for k in range(4):
            grid2[k][counter]=ans[k]
        counter-=1
    for i in range(4):
        for j in range(4):
            grid[i][j]=grid2[i][j]
    

def push_up(grid):
    """merge grid values down"""
    grid2=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    counter=0
    while counter<4:
        i=[]
        for j in grid:
            i.append(j[counter])
        ans=left_add(i)
        for k in range(4):
            grid2[k][counter]=ans[k]
        counter+=1
    for j in range(4):
        for k in range(4):
            grid[j][k]=grid2[j][k]    
        
def push_left(grid):
    """merge grid values left"""
    final_grid=[]
    for i in grid:
        final_grid.append(left_add(i))
    for i in range(4):
        for j in range(4):
            grid[i].append(final_grid[i][j])    

def push_right(grid):
    """merge grid values right"""
    final_grid=[]
    for i in grid:
        final_grid.append(right_add(i))
    for i in range(4):
        for j in range(4):
            grid[i].append(final_grid[i][j])    

#print(left_add([4,0,0,4]))
#grid1 = [[2,2,8,2],[2,8,16,8],[16,0,8,8],[4,8,2,2]]
#x=push_down(grid1)
#print(x)