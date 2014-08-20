#Kiuran Naidoo
#Assignment 7
#Question 3
#27 April 2014

def push_up(grid):#Merge Up

    for times in range(3): #Move Up
        for rows in range(3):
            for columns in range(4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows + 1][columns] = grid[rows + 1][columns], grid[rows][columns]

    for rows in range (3): #Add Adjacent cells that are the same
        for columns in range (4):
            if grid[rows][columns] == grid[rows + 1][columns] and grid[rows][columns] != 0:
                grid[rows][columns], grid[rows + 1][columns] = (grid[rows][columns])*2, 0

    for times in range (3): #Move Up Again
        for rows in range (3):
            for columns in range (4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows + 1][columns] = grid[rows + 1][columns], grid[rows][columns]

def push_down (grid): #merge down
    
    for times in range (3): #Move Down
        for rows in range (3, 0, -1):
            for columns in range (4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows -1][columns] = grid[rows-1][columns], grid[rows][columns]     
    
    for rows in range (3, 0, -1): #Add Adjacent cells that are the same
        for columns in range (4):
            if grid[rows][columns] == grid[rows - 1][columns] and grid[rows][columns] != 0:
                grid[rows][columns], grid[rows - 1][columns] = grid[rows][columns]*2, 0
                        
    for times in range (3):#Move Down
        for rows in range (3, 0, -1):
            for columns in range (4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows -1][columns] = grid[rows-1][columns], grid[rows][columns]     

        
def push_left (grid): #merge left
    
    for times in range (3): #Move Left
        for columns in range (3):
            for rows in range (4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows][columns + 1] = grid[rows][columns + 1], grid[rows][columns]
                    
    for columns in range (3):#Add Adjacent cells that are the same
        for rows in range (4):
            if grid[rows][columns] == grid[rows][columns + 1] and grid[rows][columns] != 0:
                grid[rows][columns], grid[rows][columns + 1] = grid[rows][columns]*2, 0    

    for times in range (3):#Move Left
        for columns in range (3):
            for rows in range (4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows][columns + 1] = grid[rows][columns + 1], grid[rows][columns]
                    
    
def push_right (grid): #merge right
    
    for times in range (3): #Move right
        for columns in range (3, 0, -1):
            for rows in range (4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows][columns -1] = grid[rows][columns -1], grid[rows][columns]      
    
    for columns in range (3, 0, -1): #Add adjacent cells that are the same
        for rows in range (4):
            if grid[rows][columns] == grid[rows][columns - 1] and grid[rows][columns] != 0:
                grid[rows][columns], grid[rows][columns - 1] = grid[rows][columns]*2, 0
                        
    for times in range (3):#Move Right
        for columns in range (3, 0, -1):
            for rows in range (4):
                if grid[rows][columns] == 0:
                    grid[rows][columns], grid[rows][columns -1] = grid[rows][columns -1], grid[rows][columns]      
    
  
