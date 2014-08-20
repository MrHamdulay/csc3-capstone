"""Program to add adjacent numbers to the grid
Mazwi Myeza
01 May 2014
Assignment7
Question3"""

import util

#Function to push the numbers upwards or to the left "UL" (Up,Left)
def shiftUL(grid):
     x = [] #Default array
     s = 0 #Tracer
     while s != 4: #Loop to remove "zero's" in the array
          if grid[s] != 0:
               x.append(grid[s])
          else:
               None
               
          s += 1
     while len(x) != 4:  #Loop to put the "zero's" back in
          x.append(0)
     for i in range(len(grid)): #Loop to update grid
          grid[i] = x[i]

#Function to push the numbers downwards or to the right "DR" (Down,Right)
def shiftDR(grid):
     x = []  #Default array
     s = 3   #Tracer
     while s != -1: #Loop to remove "zero's" in the array
          if grid[s] != 0:
               x.append(grid[s])
          else:
               None
               
          s -= 1
     x.reverse()     
     while len(x) != 4: #Loop to put the "zero's" back in
          x.append(0)
     x.reverse()     
     for i in range(len(grid)):  #Loop to update grid
          grid[i] = x[i]
     
     
#Function to merge the numbers if they're the same
def mergeUL(grid):
     x = [] #default array
     shiftUL(grid) #calling shift function
     for i in range(len(grid)): #Loop to merge numbers if they're the same, 
                                #discard one of them while storing their sum in 
                               #an array and also storing non-zero numbers regardless
          if i+1 < len(grid):
               if grid[i] == grid[i+1]:
                    x.append(2*grid[i])
                    grid[i+1] = 0
               else:
                    x.append(grid[i])
                    if i == 2:
                         if grid[3] != 0:
                              x.append(grid[3])
               
     
     while len(x) != 4: #putting zeros back in
          x.append(0)
     for j in range(len(grid)): #Updating grid
          grid[j] = x[j]
     shiftUL(grid)
     
def mergeDR(grid):
     #x = []  #default array
     shiftDR(grid)  #calling shift function
     for i in [3,2,1,0]:        #Loop to merge numbers if they're the same, 
                                #discard one of them while storing their sum in 
          if i - 1 >=0:                       #an array and also storing non-zero numbers regardless
     
               if grid[i] == grid[i-1]:
                    grid[i] = 2*grid[i]
                    grid[i-1] = 0
               
     shiftDR(grid) 


#Function that will merge grid values upwards
def push_up(grid):
     col1, col2 , col3, col4 = [], [], [], [] #Default arrays
     for row in range(len(grid)): #Splitting grid into separate columns
          col1.append(grid[row][0])
          col2.append(grid[row][1])
          col3.append(grid[row][2])
          col4.append(grid[row][3])
     #Calling merge function on the columns     
     mergeUL(col1)
     mergeUL(col2)
     mergeUL(col3)
     mergeUL(col4)
     #Updating grid
     for i in range(len(grid)):
          grid[i][0] = col1[i]
          grid[i][1] = col2[i]
          grid[i][2] = col3[i]
          grid[i][3] = col4[i]
     #returning grid
     return grid

#Function that will merge grid values downwards
def push_down(grid):
     #Default arrays
     col1, col2 , col3, col4 = [], [], [], []
     
     #Splitting grid into separate columns
     for row in range(len(grid)):
          col1.append(grid[row][0])
          col2.append(grid[row][1])
          col3.append(grid[row][2])
          col4.append(grid[row][3])
     #Calling merge function on the columns     
     mergeDR(col1)
     mergeDR(col2)
     mergeDR(col3)
     mergeDR(col4)
     #Updating grid   
     for i in range(len(grid)):
          grid[i][0] = col1[i]
          grid[i][1] = col2[i]
          grid[i][2] = col3[i]
          grid[i][3] = col4[i]
     #returning grid   
     return grid     

#Function that will merge grid values left    
def push_left(grid):
     #Default arrays
     row1, row2 , row3, row4 = [], [], [], [] 
     #Splitting grid into separate columns
     for col in range(len(grid)):
          row1.append(grid[0][col])
          row2.append(grid[1][col])
          row3.append(grid[2][col])
          row4.append(grid[3][col])
     #Calling merge function on the columns     
     mergeUL(row1)
     mergeUL(row2)
     mergeUL(row3)
     mergeUL(row4)
     #Updating grid       
     for i in range(len(grid)):
          grid[0][i] = row1[i]
          grid[1][i] = row2[i]
          grid[2][i] = row3[i]
          grid[3][i] = row4[i]
     #returning grid    
     return grid     

# Function that will merge grid values right     
def push_right(grid):
     
     row1, row2 , row3, row4 = [], [], [], [] #Default arrays
     #Splitting grid into separate columns
     for col in range(len(grid)):
          row1.append(grid[0][col])
          row2.append(grid[1][col])
          row3.append(grid[2][col])
          row4.append(grid[3][col])
     #Calling merge function on the columns
     mergeDR(row1)
     mergeDR(row2)
     mergeDR(row3)
     mergeDR(row4)
     #updating grid            
     for i in range(len(grid)):
          grid[0][i] = row1[i]
          grid[1][i] = row2[i]
          grid[2][i] = row3[i]
          grid[3][i] = row4[i]
     #returning grid        
     return grid     
                                                                
                                                                                 
     
            
        