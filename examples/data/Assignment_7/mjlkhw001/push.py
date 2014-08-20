# 2048 Simulator Push Module
# Khwezi Majola
# MJLKHW001
# 27 April 2014

def push_up (grid):
    """merge grid values upwards"""
    temp = [] #Empty list
    for i in range(4):
        for j in range(4):
            if grid[j][i] > 0:
                temp.append(grid[j][i]) #Extract non-zero values from column or row
        lentemp = len(temp)
        if lentemp > 0:
            for k in range(1, lentemp):
                if (temp[k] == temp[k-1]) or (temp[k-1] == 0): #Check if addition is applicable
                    temp[k-1] = temp[k] + temp[k-1] #Do the relevant addition
                    temp[k] = 0 #Replace shifted value with 0
        while 0 in temp:
            temp.remove(0) #Remove zeroes
        lentemp = len(temp)
        for k in range(4-lentemp):
            temp.append(0) #Add zeroes to the end
        for j in range(4):
            grid[j][i] = temp[j] #Replace the old values with the new
        temp = [] #Reset the list for the next row or column
    return grid
def push_down (grid):
    """merge grid values downwards"""
    temp = [] #Same as above
    for i in range(4):
        for j in range(4):
            if grid[j][i] > 0:
                temp.append(grid[j][i]) #Same as above
        lentemp = len(temp)
        if lentemp > 0:
            for k in range(lentemp-1, 0, -1): #Same as above
                if (temp[k] == temp[k-1]) or (temp[k-1] == 0):
                    temp[k] = temp[k] + temp[k-1]
                    temp[k-1] = 0
        while 0 in temp: #Same as above
            temp.remove(0)  
        lentemp = len(temp)
        
        for w in range(4-lentemp): #Adds zeroes to the beginning
            temp.insert(0, 0)            
            
        for j in range(4): #Same as above
            grid[j][i] = temp[j]
        temp = [] #Same as above
    return grid
def push_left (grid):
    """merge grid values left"""
    temp = [] #Same as above
    for i in range(4):
        for j in range(4):
            if grid[i][j] > 0:
                temp.append(grid[i][j]) #Same as above
        lentemp = len(temp)
        if lentemp > 0:
            for k in range(1, lentemp): #Same as above
                if (temp[k] == temp[k-1]) or (temp[k-1] == 0):
                    temp[k-1] = temp[k] + temp[k-1]
                    temp[k] = 0
        while 0 in temp: #Same as above
            temp.remove(0) 
        lentemp = len(temp)
        for k in range(4-lentemp): #Adds zeroes to the end
            temp.append(0)
        for j in range(4):
            grid[i][j] = temp[j] #Same as above
        temp = [] #Same as above
    return grid
def push_right (grid):
    """merge grid values right"""
    temp = [] #Same as above
    for i in range(4): 
        for j in range(4):
            if grid[i][j] > 0:
                temp.append(grid[i][j]) #Same as above
        lentemp = len(temp)
        if lentemp > 0:
            for k in range(lentemp-1, 0, -1): #Same as above
                if (temp[k] == temp[k-1]) or (temp[k-1] == 0):
                    temp[k] = temp[k] + temp[k-1]
                    temp[k-1] = 0
        while 0 in temp: #Same as above
            temp.remove(0)
        lentemp = len(temp)
        
        for w in range(4-lentemp): #Adds zeroes to the beginning
            temp.insert(0, 0)
    
        for j in range(4): #Same as above
            grid[i][j] = temp[j]
        temp = [] #Same as above
    return grid