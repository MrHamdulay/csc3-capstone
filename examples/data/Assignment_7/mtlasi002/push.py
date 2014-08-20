#Asil Motala
#MTLASI002
#Assignment 7
#Question 3
#27 April 2014

def push_up (grid):
    
    for column in range(4):                                     #loop through each column
        for row in range(3):                                    #loop through each row
            counter=1                                           #intialize counter variable for while loop
            while counter<(4-row) and grid[row][column]==0:     #pre-test for loop
                grid[row][column]=grid[row+counter][column]     #assign grid position a new grid position below it
                grid[row+counter][column]=0                     #remove the old grid position
                counter+=1                                      #update counter variable
    
    for column in range(4):                                     #loop through each column
        for row in range(3):                                    #loop through each row
            if grid[row][column]==grid[row+1][column]:          #check if adjacent value underneath is equal 
                grid[row][column]=2*grid[row][column]           #replace intial value with sum of value
                grid[row+1][column]=0                           #replace adjacent value with 0

    for column in range(4):                                     #loop through each column
        for row in range(3):                                    #loop through each row
            counter=1                                           #intialize counter variable for while loop
            while counter<(4-row) and grid[row][column]==0:     #pre-test for loop
                grid[row][column]=grid[row+counter][column]     #assign grid position a new grid position below it
                grid[row+counter][column]=0                     #remove the old grid position
                counter+=1                                      #update counter variable

def push_down (grid):
    
    for column in range(4):                                     #loop through each column
        for row in range(3,0,-1):                               #loop through each row
            counter=1                                           #intialize counter variable for while loop
            while counter<(row+1) and grid[row][column]==0:     #pre-test for loop
                grid[row][column]=grid[row-counter][column]     #assign grid position a new grid position above it
                grid[row-counter][column]=0                     #remove the old grid position
                counter+=1                                      #update counter variable
    
    for column in range(4):                                     #loop through each column
        for row in range(3,0,-1):                               #loop through each row
            if grid[row][column]==grid[row-1][column]:          #check if adjacent value above is equal 
                grid[row][column]=2*grid[row][column]           #replace intial value with sum of value
                grid[row-1][column]=0                           #replace adjacent value with 0

    for column in range(4):                                     #loop through each column
        for row in range(3,0,-1):                               #loop through each row
            counter=1                                           #intialize counter variable for while loop
            while counter<(row+1) and grid[row][column]==0:     #pre-test for loop
                grid[row][column]=grid[row-counter][column]     #assign grid position a new grid position above it
                grid[row-counter][column]=0                     #remove the old grid position
                counter+=1                                      #update counter variable

def push_left (grid):
    
    for row in range(4):                                        #loop through each row
        for column in range(3):                                 #loop through each column
            counter=1                                           #intialize counter variable for while loop
            while counter<(4-column) and grid[row][column]==0:  #pre-test for loop
                grid[row][column]=grid[row][column+counter]     #assign grid position a new grid position right of it
                grid[row][column+counter]=0                     #remove the old grid position
                counter+=1                                      #update counter variable
    
    for row in range(4):                                        #loop through each row
        for column in range(3):                                 #loop through each column
            if grid[row][column]==grid[row][column+1]:          #check if adjacent value right of it is equal 
                grid[row][column]=2*grid[row][column]           #replace intial value with sum of value
                grid[row][column+1]=0                           #replace adjacent value with 0

    for row in range(4):                                        #loop through each row
        for column in range(3):                                 #loop through each column
            counter=1                                           #intialize counter variable for while loop
            while counter<(4-column) and grid[row][column]==0:  #pre-test for loop
                grid[row][column]=grid[row][column+counter]     #assign grid position a new grid position right of it
                grid[row][column+counter]=0                     #remove the old grid position
                counter+=1                                      #update counter variable

def push_right (grid):
        
    for row in range(4):                                        #loop through each row
        for column in range(3,0,-1):                                 #loop through each column
            counter=1                                           #intialize counter variable for while loop
            while counter<(column+1) and grid[row][column]==0:  #pre-test for loop
                grid[row][column]=grid[row][column-counter]     #assign grid position a new grid position right of it
                grid[row][column-counter]=0                     #remove the old grid position
                counter+=1                                      #update counter variable
    
    for row in range(4):                                        #loop through each row
        for column in range(3,0,-1):                                 #loop through each column
            if grid[row][column]==grid[row][column-1]:          #check if adjacent value right of it is equal 
                grid[row][column]=2*grid[row][column]           #replace intial value with sum of value
                grid[row][column-1]=0                           #replace adjacent value with 0

    for row in range(4):                                        #loop through each row
        for column in range(3,0,-1):                                 #loop through each column
            counter=1                                           #intialize counter variable for while loop
            while counter<(column+1) and grid[row][column]==0:  #pre-test for loop
                grid[row][column]=grid[row][column-counter]     #assign grid position a new grid position right of it
                grid[row][column-counter]=0                     #remove the old grid position
                counter+=1                                      #update counter variable
