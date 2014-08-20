""" Tumi Mkhawana
16 May 2014
Assignment 9 Question 3"""

#create an empty list
grid=[]
#for i in range(9):
    #grid.append([i]*9)
#for i in range(9):
    #print(grid[i])

for i in range(9):
    x = input()
    sub=[]
    for k in x:
        sub.append(k)
    grid.append(sub)

#check if there are repeats in rows
def row(grid):
    win=True
    for k in grid:
        found = ''
        for i in k:
            #check if any repeats are found
            if found.find(str(i))>-1:
                found ='Lost'
                break
            else:
                found+=str(i)
                #check if any repeats are found
        if found.find('Lost')>-1:
            win=False
    return win

#check if there are repeats in columns
def col(grid):
    win=True
    for i in range(9):
        found = ''
        for k in range(9):
            #check if any repeats are found
            if found.find(str(grid[k][i]))>-1:
                found ='Lost'
                break
            else:
                found+=str(grid[k][i])
                #check if any repeats are found
        if found.find('Lost')>-1:
            win=False
    return win    

#check if there are repeats in 3*3 grids
def gridX(grid):
    win = True
    for row in range(0,9,3):
        for col in range(0,9,3):
            found = ''
            for i in range(row,row+3):
                for k in range(col,col+3):
                    #check if any repeats are found
                    if found.find(str(grid[i][k]))>-1:
                        found ='Lost'
                        break
                    else:
                        found+=str(grid[i][k])
                        #check if any repeats are found
                if found.find('Lost')>-1:
                    win=False
                    break
    return win    

#if any repeats are invalid, print invalid
if gridX(grid)==False or row(grid)==False or col(grid)==False:
    print('Sudoku grid is not valid')
    #else if all are valid, print valid
else:
    print('Sudoku grid is valid')
                        
                        
                        
                    
                    
            
            
            
        
    