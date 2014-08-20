#Write a program to check if a complete Sudoku grid is valid or not.

#A Sudoku grid is a 9x9 grid of integers, with each cell containing an integer value from 1-9. 
#The input to your program is a set of nine lines, each containing 9 single digit integers with no intervening spaces. 
#Your program must store these integers internally in a 2-dimensional array.

#In a correct Sudoku solution, the following conditions hold:

#no 2 cells in the same row have the same value
#no 2 cells in the same column have the same value
#no 2 cells in the same 3x3 sub-grid have the same value - this is tested for the 9 non-overlapping sub-grids that a 9x9 grid can be divided into

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 11 May 2014


def split_string(array):
    """Splits each item in an array into individual lists separated by comma's"""
    
    for i in range(len(array)):
        if len(array[i]) != len(array):
            array[i] = list(array[i]) # Convert each element into a list
    return array
        
def create_grid(n):
    """Create a matrix of length n"""
    array = []
    for i in range(n):
        array.append([0]*n)
    return array

def transpose_grid(array):
    """Convert rows of a matrix to columns"""
    temp = create_grid(9)
    
    for i in range(len(array)):
        for j in range(len(array)):
            temp[i][j] = array[j][i]
    return temp



def main():
    
    grid = []#['752639841','348751926','169284573','923146785','481975362','675823194','816392457','294517638','537468219']
    # Wait for input until 9 lines are entered
    while len(grid) != 9:
        grid.append(input())    
    #print(grid)
    # Split each element into a list of length equal to the main matrix
    splited = transpose_grid(grid)
    #print(splited)
    grid = transpose_grid(splited)    
    #print (grid)
    # Transpose the grid to start comparing rows and columns
    trans = transpose_grid(grid)
    #print(trans)
    
    
    totalr,totalc = 0,0
    # Calculate the sum of all the numbers in the grid
    for i in range(len(splited)):
        for j in range(len(trans)):
            totalr += int(splited[i][j]) # Sum the rows
            totalc += int(trans[i][j])  # Sum the columns
            #print(i,totalr,totalc)
        if totalr != 45 or  totalc != 45:
            #print(i,totalr,totalc)
            break        
        totalc = 0
        totalr = 0    
    
    # Calculate the sum of all 9 cells
    cells = True
    cell1,cell2,cell3,cell4,cell5,cell6,cell7,cell8,cell9 = 0,0,0,0,0,0,0,0,0
    
    for c in range(3):
        cell1 += int(grid[0][c])
        cell1 += int(grid[1][c])
        cell1 += int(grid[2][c])
        cell2 += int(grid[3][c])
        cell2 += int(grid[4][c])
        cell2 += int(grid[5][c])
        cell3 += int(grid[6][c])
        cell3 += int(grid[7][c])
        cell3 += int(grid[8][c])
        cell4 += int(grid[0][c+3])
        cell4 += int(grid[1][c+3])
        cell4 += int(grid[2][c+3])
        cell5 += int(grid[3][c+3])
        cell5 += int(grid[4][c+3])
        cell5 += int(grid[5][c+3])
        cell6 += int(grid[6][c+3])
        cell6 += int(grid[7][c+3])
        cell6 += int(grid[8][c+3])
        cell7 += int(grid[0][c+6])
        cell7 += int(grid[1][c+6])
        cell7 += int(grid[2][c+6])
        cell8 += int(grid[3][c+6])
        cell8 += int(grid[4][c+6])
        cell8 += int(grid[5][c+6])
        cell9 += int(grid[6][c+6])
        cell9 += int(grid[7][c+6])
        cell9 += int(grid[8][c+6])
    #print(cell1,cell4,cell7)
    #print(cell2,cell5,cell8)
    #print(cell3,cell6,cell9)        
    
    
    # Checks if any of the cells have duplicate numbers
    if (cell1 == 45) and (cell2 == 45) and (cell3 == 45) and (cell4 == 45) and (cell5 == 45) and (cell6 == 45) and (cell7 == 45) and (cell8 == 45) and (cell9 == 45):        
        cells = True # Sum of all cells is 45
    else:        
        cells = False # Some cells have missing numbers
    
    if (totalr == totalc) and cells == True: # Check if sum of all rows, columns and cells is 45
        print("Sudoku grid is valid")
    else: 
        print("Sudoku grid is not valid")
        
            
if __name__ == "__main__":
    main()


     
#Sample I/O:

#359716482 || 384351967 
#867345912 || 561947823
#413928675 || 973862415
#398574126 || 739526184 
#546281739 || 142783659
#172639548 || 658419372
#984163257 || 496175238 
#621857394 || 817234596
#735492861 || 225698741
#Sudoku grid is not valid

#Sample I/O:

#259716483 || 284351967
#867345912 || 561947823
#413928675 || 973862415
#398574126 || 739526184
#546281739 || 142783659
#172639548 || 658419372
#984163257 || 496175238
#621857394 || 817234596
#735492861 || 325698741
#Sudoku grid is valid