'''Module with push functions for 2048
Tinotenda Chemvura CHMTIN004
01 May 2014'''

#_______________________________Program Starts Here___________________________________
from copy import deepcopy

def push_up (grid):
    """merge grid values upwards"""
    #push all the values up
    #go through every column, if an item = 0, look for the next non zero item and replace the first item with the 2nd one
    #change the 2nd item to zero
    for i in range(0,4):
        for j in range(0,4):
            if grid[j][i] == 0:
                for k in range(j+1,4):
                    if grid[k][i] != 0:
                        grid[j][i] = grid[k][i]
                        grid[k][i] = 0
                        break
    #add adjacent identical numbers and replace the second one with a zero    
    for i in range(0,4):
        for j in range(0,3):
            if grid[j][i] == grid[j+1][i]:
                new_add = grid[j][i] * 2
                grid[j][i] = new_add
                grid[j+1][i] = 0
#shift the numbers again

    for i in range(0,4):
        for j in range(0,4):
            if grid[j][i] == 0:
                for k in range(j+1,4):
                    if grid[k][i] != 0:
                        grid[j][i] = grid[k][i]
                        grid[k][i] = 0
                        break               
    #return grid
#________________________________________________________________________________________________________________________
def push_down (grid):
    """merge grid values downwards"""
    #go through every column, if an item = 0, look for the next non zero item and replace the first item with the 2nd one
       #change the 2nd item to zero    

    for i in range(0,4):
        for j in range(3,-1,-1):
            if grid[j][i] == 0:
                for k in range(j-1,-1,-1):
                    if grid[k][i] != 0:
                        grid[j][i] = grid[k][i]
                        grid[k][i] = 0
                        break
    #add adjascent identical numbers and replace the old cell with a zero
    for i in range(0,4):
        for j in range(3,-1,-1):
            if grid[j][i] == grid[j-1][i]:
                new_add = grid[j][i] * 2
                grid[j][i] = new_add
                grid[j-1][i] = 0
            else:
                grid[j][i] = grid[j][i]       
    #shift the numbers again
    for i in range(0,4):
        for j in range(3,-1,-1):
            if grid[j][i] == 0:
                for k in range(j-1,-1,-1):
                    if grid[k][i] != 0:
                        grid[j][i] = grid[k][i]
                        grid[k][i] = 0
                        break
    
    #return grid
#________________________________________________________________________________________________________________________
def push_left (grid):
    """merge grid values left"""
    #push all values to the left
    #loop thru each value in a row, if value = 0, start anothr loop from that current cell to the end until u find a number not = 0, replace tht old cell with the new cell.
        
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j] == 0:
                for k in range(j+1,4):
                    if grid[i][k] != 0:
                        grid[i][j] = grid[i][k]
                        grid[i][k] = 0
                        break
    #add adjascent identical number and replace old cell with zero
    for i in range(0,4):
        for j in range(0,3):
            if grid[i][j] == grid[i][j+1]:
                new_add = grid[i][j] * 2
                grid[i][j] = new_add
                grid[i][j+1] = 0
    #shift the numbers again
    for i in range(0,4):
        for j in range(0,4):
            if grid[i][j] == 0:
                for k in range(j+1,4):
                    if grid[i][k] != 0:
                        grid[i][j] = grid[i][k]
                        grid[i][k] = 0
                        break
    
    #return grid
#________________________________________________________________________________________________________________________

def push_right (grid):
    """merge grid values right"""     
    #push all values to the right
    #loop thru each value in a row from right to left, if value = 0, start anothr loop from that current cell to the end until u find a number not = 0, replace tht old cell with the new cell.    

    for i in range(0,4):
        for j in range(3,-1,-1):
            if grid[i][j] == 0:
                for k in range(j-1,-1,-1):
                    if grid[i][k] != 0:
                        grid[i][j] = grid[i][k]
                        grid[i][k] = 0
                        break
     #add adjascent identical numbers and replace the 2nd cell with a zero
    for i in range(0,4):
        for j in range(3,-1,-1):
            if grid[i][j] == grid[i][j-1]:
                new_add = grid[i][j] * 2
                grid[i][j-1] = new_add
                grid[i][j] = 0
                
    #shift the numbers again
    for i in range(0,4):
        for j in range(3,-1,-1):
            if grid[i][j] == 0:
                for k in range(j-1,-1,-1):
                    if grid[i][k] != 0:
                        grid[i][j] = grid[i][k]
                        grid[i][k] = 0
                        break
#_________________________________Program Ends Here________________________________________________________

#Testing codes#
#form = "{0:<5}"                     #format for the column width of 5
 #   print("+--------------------+")
  #  for row in grid:                    #go through the four lists (rows)
   #     print("|",end = "")
    #    for column in row:              #go through the 4 contents of the current list(row)
     #       if column == 0:
      #          column = " "
       #         print(form.format(column),end = "")        #the print function for each content of the grid
        #    else:
         #       print(form.format(column),end = "")
        #print("|")        
    #print("+--------------------+")