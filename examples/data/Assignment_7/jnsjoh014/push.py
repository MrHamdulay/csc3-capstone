__author__ = 'JNSJOH014'
"""Library of merging functions for use in the game 2048
28/04/2014"""
import util

def push_up (grid):
    #util.print_grid(grid)
    #Move tiles into empty spaces
    for outer in range(4):
        for inner in range(3):
            temp=0
            while grid[inner][outer]==0:
                counter = 1
                while (inner+counter)<4:
                    grid[inner+counter-1][outer]= grid[inner+counter][outer]
                    grid[inner+counter][outer] = 0
                    counter+=1
                temp+=1
                if temp>3:
                    break
    #Merge tiles
    for outer in range(4):
        for inner in range(3):
            temp=0
            if grid[inner][outer]==grid[inner+1][outer]:
                grid[inner][outer] *=2
                grid[inner+1][outer] = 0
                temp+=1
                if temp>3:
                    break
    #util.print_grid(grid)
    #Move tiles into empty spaces
    for outer in range(4):
        for inner in range(3):
            temp=0
            while grid[inner][outer]==0:
                counter = 1
                while (inner+counter)<4:
                    grid[inner+counter-1][outer]= grid[inner+counter][outer]
                    grid[inner+counter][outer] = 0
                    counter+=1
                temp+=1
                if temp>3:
                    break
def push_down(grid):
    #util.print_grid(grid)
    #Move tiles into empty spaces
    for outer in range(4):
        for inner in range(3,0,-1):
            temp=0
            while grid[inner][outer]==0:
                counter = 1
                while (inner-counter)>=0:
                    grid[inner+1-counter][outer]= grid[inner-counter][outer]
                    grid[inner-counter][outer] = 0
                    counter+=1
                temp+=1
                if temp>3:
                    break
    #Merge tiles
    for outer in range(4):
        for inner in range(3,0,-1):
            temp=0
            if grid[inner-1][outer]==grid[inner][outer]:
                grid[inner][outer] *=2
                grid[inner-1][outer] = 0
                temp+=1
                if temp>3:
                    break
    #util.print_grid(grid)
    #Move tiles into empty spaces
    for outer in range(4):
        for inner in range(3,0,-1):
            temp=0
            while grid[inner][outer]==0:
                counter = 1
                while (inner-counter)>=0:
                    grid[inner+1-counter][outer]= grid[inner-counter][outer]
                    grid[inner-counter][outer] = 0
                    counter+=1
                temp+=1
                if temp>3:
                    break

def push_left(grid):
    #util.print_grid(grid)
    #Move tiles into empty spaces
    for row in range(4):
        for column in range(3):
            temp=0
            while grid[row][column]==0:
                counter = 1
                while (column+counter)<4:
                    grid[row][column+counter-1]= grid[row][column+counter]
                    grid[row][column+counter] = 0
                    counter+=1
                temp+=1
                if temp>3:
                    break
    #util.print_grid(grid)
    #Merge tiles
    for row in range(4):
        for column in range(3):
            temp=0
            if grid[row][column]==grid[row][column+1]:
                grid[row][column] *=2
                grid[row][column+1] = 0
                temp+=1
                if temp>3:
                    break
    #util.print_grid(grid)
    #Move tiles into newly emptied spaces
    for row in range(4):
        for column in range(3):
            temp=0
            while grid[row][column]==0:
                counter = 1
                while (column+counter)<4:
                    grid[row][column+counter-1]= grid[row][column+counter]
                    grid[row][column+counter] = 0
                    counter+=1
                temp+=1
                if temp>3:
                    break
    #util.print_grid(grid)

def push_right(grid):
    #util.print_grid(grid)
    tempgrid = [[],[],[],[]]
    #util.create_grid(tempgrid)
    #util.print_grid(tempgrid)
    for row in range(4):
        temprow = []
        for col in range(4):
            temprow.append(grid[row][3-col])
        #print(temprow)
        tempgrid[row] = temprow
    #util.print_grid(tempgrid)    #util.print_grid(tempgrid)
    push_left(tempgrid)
    #util.print_grid((tempgrid))
    for row in range(4):
        grid[row] = []
        for col in range(4):
            grid[row].append(tempgrid[row][3-col])

    #util.print_grid(grid)

