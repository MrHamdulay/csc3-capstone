'''The soduku grid
Ednecia Matlapeng
12 May 2014 SC1015F'''
import math
#So I am gonna generate a 9*9 grid to check
grid,mini =[],[]
line = ''

for i in range(9):
    line = input()
    for k in range(9):
        mini.append(int(line[k]))
   # print(grid)
    grid.append(mini[0:9])
    mini=[]
#The vertical check, no repeats on this line

def vertical(grid):
    vert = ''# Keeps track of all the values already found
    for i in range(len(grid)):
        vert = ''
        horiz = ''
        for k in range(len(grid[i])):
            if vert.find(str(grid[i][k]))>-1:#Number in grid line already
                vert = 'Lost'
                break
               
            else:
                vert+=str(grid[i][k])
    if vert.find('Lost')>-1:
        return False
    else:
        return True
    
        
#print(vertical(grid))   
#Check on the horizontal side
def horizontal(grid):
    horiz= ''
    for i in range(len(grid)):
        horiz = ''
        for k in range(len(grid[i])):
            if horiz.find(str(grid[k][i]))>-1:#Number in grid line already
                horiz = 'Lost'
                break
               
            else:
                horiz+=str(grid[k][i])
    if horiz.find('Lost')>-1:
        return False
    else:
        return True    
#print(horizontal(grid))

#Check the values in the block repeat check, ok I need help here. for real
def block(grid):
    lost = ''
    for  block in range(0,9,3):
        #The grid moves left
        for wblock in range(0,9,3):
            #The grid moves right
            found = ''
            for i in range(block,block+3):
                #Move within that grid
                for w in range(wblock,wblock+3):
                    if found.find(str(grid[i][w]))>-1:
                        lost = 'Lost'
                        break
                    else:
                        found+=str(grid[i][w])
            if lost.find('Lost')>-1:
                break
    if lost =='':
        return True
    else:
        return False
#Now I print the output
if block(grid)== False or vertical(grid)== False or horizontal(grid)== False:
    print('Sudoku grid is not valid')
else:
    print('Sudoku grid is valid')
    

    

            
    
    