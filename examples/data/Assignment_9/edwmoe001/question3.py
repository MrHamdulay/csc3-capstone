"""Sudoku grid checker
Tauhirah Eguardo
2014/05/12"""

def vert(array):
    #creates array to check if values are equal vertically
    grid = []
    for i in range(9):
        line = []
        for j in range(9):
            line.append(array[j][i])
        grid.append(line)
    return grid
            
def tester(array):
    #tests to see if array[i] != array[i+1]
    won = True
    for i in range(9):
        if won == True:
            for j in range(8):
                if array[i][j] == array[i][j+1]:
                    won = False
                    break
                else:
                    pass
        else:
            break
    return won
            
                
    
def multi_input():
    #allows input to be inputted as it is multiline
    array = []
    for i in range(9):
        array.append(input())
    return array
    
def block(array):
    """tests to see if 3*3 blocks are equal"""
    grid = []
    for z in range(0,7,3): #0,3,6
        #vertical down 3
        for n in range(0,7,3): #0,3,6
            #horiz across 3
            line = []
            for i in range(3):
                for j in range(3):
                    vert,hor = i+z,j+n
                    line.append(array[vert][hor])
            grid.append(line)
    won = True
    for i in range(len(grid)):
        if won == True:
            if len(grid[i]) != len(set(grid[i])):
                won = False
            else:
                pass
        else:
            break
    return won
                  
        
        
def main():
    array = multi_input()
    for i in range(len(array)):
        array[i] = list(array[i])
    vert_array = vert(array)
    block(array)
    if tester(array) == True and tester(vert_array) == True and block(array) == True: #checks if no adjacent equal values in arrays
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

main()