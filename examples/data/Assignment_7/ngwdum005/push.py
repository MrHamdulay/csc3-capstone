'''Dumisani Ngwenza
30/04/2014
NGWDUM005
Assignment 7 Question 3'''

def push_up (grid):
    '''merge grid values upwards'''
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    
    row1.append(grid[0])
    row2.append(grid[1])
    row3.append(grid[2])
    row4.append(grid[3])
    for i in range (4):
        if row1[0][i] == 0:
            row1[0][i] = row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == 0:
            row2[0][i] = row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == 0:
            row3[0][i] = row4[0][i]
            row4[0][i] = 0
        if row1[0][i] == 0 and row2[0][i] == 0:
            row1[0][i] = row3[0][i]
            row3[0][i] = 0
        if row2[0][i] == 0 and row3[0][i] == 0:
            row2[0][i] = row4[0][i] 
            row4[0][i] = 0
     
    for i in range (4):
        if row1[0][i] == 0:
            row1[0][i] = row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == 0:
            row2[0][i] = row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == 0:
            row3[0][i] = row4[0][i]
            row4[0][i] = 0
        if row1[0][i] == 0 and row2[0][i] == 0:
            row1[0][i] = row3[0][i]
            row3[0][i] = 0
        if row2[0][i] == 0 and row3[0][i] == 0:
            row2[0][i] = row4[0][i] 
            row4[0][i] = 0   
    
    for i in range (4):
        if row1[0][i] == 0:
            row1[0][i] = row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == 0:
            row2[0][i] = row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == 0:
            row3[0][i] = row4[0][i]
            row4[0][i] = 0
        if row1[0][i] == 0 and row2[0][i] == 0:
            row1[0][i] = row3[0][i]
            row3[0][i] = 0
        if row2[0][i] == 0 and row3[0][i] == 0:
            row2[0][i] = row4[0][i] 
            row4[0][i] = 0
            
    for i in range (4):
        if row1[0][i] == row2[0][i]:
            row1[0][i] = row1[0][i] + row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == row3[0][i]:
            row2[0][i] = row2[0][i] + row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == row4[0][i]:
            row3[0][i] = row3[0][i] + row4[0][i]
            row4[0][i] = 0
    grid = [row1[0], row2[0], row3[0], row4[0]]        
    #print (row1, row2, row3, row4)
    return grid
    

def push_down (grid):
    '''merge grid values downwards'''
    row1 = []
    row2 = []
    row3 = []
    row4 = []    
    row1.append(grid[0])
    row2.append(grid[1])
    row3.append(grid[2])
    row4.append(grid[3])    
    for i in range (4):
        #print (grid[i])
        if row4[0][i] == 0:
            row4[0][i] = row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == 0:
            row3[0][i] = row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == 0:
            row2[0][i] = row1[0][i]
            row1[0][i] = 0
        if row4[0][i] == 0 and row3[0][i] == 0:
            row4[0][i] = row2[0][i]
            row2[0][i] = 0
        if row3[0][i] == 0 and row2[0][i] == 0:
            row3[0][i] = row1[0][i]
            row1[0][i] = 0
    
    for i in range (4):
        if row4[0][i] == 0:
            row4[0][i] = row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == 0:
            row3[0][i] = row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == 0:
            row2[0][i] = row1[0][i]
            row1[0][i] = 0
        if row4[0][i] == 0 and row3[0][i] == 0:
            row4[0][i] = row2[0][i]
            row2[0][i] = 0
        if row3[0][i] == 0 and row2[0][i] == 0:
            row3[0][i] = row1[0][i]
            row1[0][i] = 0   
            
    for i in range (4):
        if row4[0][i] == 0:
            row4[0][i] = row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == 0:
            row3[0][i] = row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == 0:
            row2[0][i] = row1[0][i]
            row1[0][i] = 0
        if row4[0][i] == 0 and row3[0][i] == 0:
            row4[0][i] = row2[0][i]
            row2[0][i] = 0
        if row3[0][i] == 0 and row2[0][i] == 0:
            row3[0][i] = row1[0][i]
            row1[0][i] = 0 
        
    for i in range (4):
        if row4[0][i] == row3[0][i]:
            row4[0][i] += row3[0][i]
            row3[0][i] = 0
        if row3[0][i] == row2[0][i]:
            row3[0][i] += row2[0][i]
            row2[0][i] = 0
        if row2[0][i] == row1[0][i]:
            row2[0][i] += row1[0][i]
            row1[0][i] = 0
    
    grid = [row1[0], row2[0], row3[0], row4[0]]
    return grid
    
def push_left (grid):
    '''merge grid values left'''
    
def push_right (grid):
    '''merge grid values right'''
    

if __name__=='__main__':
    grid = [[2,0,2,0],[0,4,0,8],[0,16,0,128],[2,2,2,2]]
    print (push_up(grid))
    print (push_down(grid))