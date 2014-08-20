"""Assignment 7 Question 3
James Lloyd
28 April 2014"""

def push_up (grid):
    """merge grid values upwards"""
    for i in range (4):
        #Create new row to merge. Merging is done row by row or column by column
        row = []
        for j in range (4):
            #Filling row
            row.append (grid [j][i])
        #Mergin row    
        merge (row)
        
        for h in range (4):
            #Filling old grid with new merged row
            grid [h][i] = row [h]
        
                
def push_down (grid):
    """merge grid values downwards"""
    for i in range (4):
        row = []
        for j in range (3, -1, -1):
            row.append (grid [j][i])
        merge (row)
        
        for h in range (3,-1,-1):
            #3 - j to fill the column in reverse order to row
            grid [h][i] = row [3 - h]

def push_left (grid):
    """merge grid values left""" 
    for i in range (4):
        row = []
        for j in range (4):
            row.append (grid [i][j])
        merge (row)
        for h in range (4):
            grid [i][h] = row [h]
        

def push_right (grid):
    """merge grid values right"""
    for i in range (4):
        row = []
        for j in range (3, -1, -1):
            row. append (grid [i][j])
        merge (row)
        
        for h in range (3, -1, -1):
            grid [i][h] = row [3 - h]

def merge (row):
    #Remove gaps between numbers
    for x in range (3):
        for i in range (3):
            if row [i] == 0:
                row [i] = row [i + 1]
                row [i + 1] = 0
    
    #Add same adjacent number
    for i in range (3):
        if row [i] == row [i + 1]:
            row [i] = 2 * row [i]
            row [i + 1] = 0
            
    #Remove new gaps
    for x in range (3):
        for i in range (3):
            if row [i] == 0:
                row [i] = row [i + 1]
                row [i + 1] = 0  
    
