# This module contains four functions that push elements in a grid as in 2048 game
# push_up - merge grid values upwards
# push_down - merge grid values downwards
# push_left - merge grid values left
# push_right - merge grid values right
# The four functions above use function below to achieve to the movements
# transposed - exchange rows with columns
# remove_zero - removes moves all zero's in the matix
# add_zero - adds a zero to every row of the array with length not equal to the array
# add_zero_right - moves all zero's to the far right
# add_zero_left - moves all zero's to the far right
# add_left - adds equal adjacent values and puts result to the left and replace old position with zero
# add_right - adds equal adjacent values and puts result to the right and replace old position with zero
# modify_grid - copy content from array to the other

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 02 May 2014

def transposed(grid):
    """exchange rows with columns"""
    
    gray=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]    
    for i in range(4):
        for j in range(4):
            gray[i][j] = grid[j][i] #exchange rows with columns
    
    return gray


def remove_zero(grida):
    """removes moves all zero's in the matix"""
    
    nozero = [[],[],[],[]] #create a temporary empty grid        
    # this loop copies non zero values to the temporary list
    for i in range(len(grida)):
        for j in range(len(grida)):
            if grida[i][j] != 0:
                nozero[i].append(grida[i][j])
                
    return nozero


def add_zero(gray):
    """adds a zero to every row of the array with length not equal to the array"""
    
    for i in range(len(gray)):
        while len(gray[i]) != len(gray):
            gray[i].append(0)
            
    return gray


def add_zero_right(gridb):
    """moves all zero's to the far right"""
    
    mover = [[],[],[],[]] #create a temporary empty grid        
    # this loop copies non zero values to the temporary list mover
    for i in range(len(mover)):
        for j in range(len(gridb[i])):
            mover[i].append(gridb[i][j])
        
        while len(mover[i]) != len(gridb):
            #add extra zero until both lists are of equal length
            mover[i].append(0)    
    
    return mover


def add_zero_left(gridc):
    """moves all zero's to the far right"""
    
    movel = [[],[],[],[]] #create a temporary empty grid        
    # this loop copies non zero values to the temporary list movel
    for i in range(len(movel)):
        for j in range(len(gridc[i])):
            movel[i].append(gridc[i][j])
                
        while len(movel[i]) != len(gridc):
            #add extra zero until both lists are of equal length
            movel[i].insert(0,0)    
    
    return movel


def add_left(gridd):
    """adds equal adjacent values and puts result to the left and replace old position with zero"""
    for i in range(len(gridd)):
        for j in range(len(gridd[i])-1):
            if gridd[i][j] == gridd[i][j+1]:
                #add left most number and replace number on the right with zero
                gridd[i][j],gridd[i][j+1] = 2*gridd[i][j],0  
    
    return gridd


def add_right(gride):
    """adds equal adjacent values and puts result to the right and replace old position with zero"""
    for i in range(len(gride)):
        for j in range(len(gride[i])-1,0,-1):
            if gride[i][j] == gride[i][j-1]:
                #add right most number and replace number on the left with zero
                gride[i][j],gride[i][j-1] = 2*gride[i][j],0
    
    return gride


def modify_grid(temp,grid):
    """copy content from array (temp) to array (grid)"""
    for i in range(len(temp)):
        for j in range(len(temp)):
            grid[i][j] = temp[i][j]    


def push_up (grid):
    """merge grid values upwards"""
    
    tempu = grid #pass parameter to local variable for manipulation
    tempu = transposed(tempu) #transpose the matrix to change columns into rows
    #push the matrix to the left
    tempu = remove_zero(tempu) #remove zeros in the matrix
    tempu = add_left(tempu) #add equal adjacent values starting from the left
    tempu = add_zero(tempu) #add zero to each row until it has 4 elements
    tempu = remove_zero(tempu) #remove zeros in the matrix
    tempu = add_zero_right(tempu) #add zeros on the right 
    tempu = transposed(tempu) #transpose the matrix to change rows into columns
    modify_grid(tempu,grid) #add contents from tempu to grid    


def push_down (grid):
    """merge grid values downwards"""
    
    tempd = grid #pass parameter to local variable for manipulation
    tempd = transposed(tempd) #transpose the matrix to change columns into rows
    #push the matrix to the right
    tempd = remove_zero(tempd) #remove zeros in the matrix
    tempd = add_right(tempd) #add equal adjacent values starting from the right
    tempd = add_zero(tempd) #add zero to each row until it has 4 elements
    tempd = remove_zero(tempd) #remove zeros in the matrix
    tempd = add_zero_left(tempd) #add zeros on the left  
    tempd = transposed(tempd) #transpose the matrix to change rows into columns
    modify_grid(tempd,grid) #add contents from tempd to grid


def push_left (grid):
    """merge grid values left"""
    
    templ = grid #pass parameter to local variable for manipulation
    templ = remove_zero(templ) #remove zeros in the matrix
    templ = add_left(templ) #add equal adjacent values starting from the left
    templ = add_zero(templ) #add zero to each row until it has 4 elements
    templ = remove_zero(templ) #remove zeros in the matrix
    templ = add_zero_right(templ) #add zeros on the right
    modify_grid(templ,grid) #add contents from templ to grid    


def push_right (grid):
    """merge grid values right"""  
    
    tempr = grid #pass parameter to local variable for manipulation
    tempr = remove_zero(tempr) #remove zeros in the matrix
    tempr = add_right(tempr) #add equal adjacent values starting from the right
    tempr = add_zero(tempr) #add zero to each row until it has 4 elements
    tempr = remove_zero(tempr) #remove zeros in the matrix
    tempr = add_zero_left(tempr) #add zeros on the left
    modify_grid(tempr,grid) #add contents from tempr to grid



#Sample I/O:

# +--------------------+
# |                    |
# |                    |
# |          2         |
# |2                   |
# +--------------------+
# Enter a direction:
# l
# +--------------------+
# |                    |
# |                    |
# |2                   |
# |2         2         |
# +--------------------+
# Enter a direction:
# u
# +--------------------+
# |4         2         |
# |                    |
# |                    |
# |     4              |
# +--------------------+
# Enter a direction:
# d
# +--------------------+
# |     2              |
# |                    |
# |                    |
# |4    4    2         |
# +--------------------+
# Enter a direction:
# r
# +--------------------+
# |               2    |
# |                    |
# |     2              |
# |          8    2    |
# +--------------------+
# Enter a direction:
# x