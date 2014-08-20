"""A program to check if a Sudoku grid is valid or not
simlindile mahlaba
14 May 2014"""

def main():  
    sudokuGrid = []  
    valid = True  
    for x in range(8):
        sudokuGrid.append([])
        line = input("")
        for y in range(8):
            number = line[y]
            if line.count(number)>1:  
                valid = False 
            sudokuGrid[x].append(number)
            
    if valid==False:
        print("Sudoku grid is not valid")
    else:
        print("Sudoku grid is valid")
#checks columns
def column(sudokuGrid,valid):
    
    for x in range(8):
        line=""  
        for y in range(8):
            line+=sudokuGrid[y][x]   
        for z in range(8):
            number = line[z]
            if line.count(number)>1:
                valid = False
                  
    return valid

#checks 3x3 blocks
def blocks(sudokuGrid, valid):   
    for x in range(0,9,3): 
        block=""
        for y in range(x,x+3):
            for z in range(y,y+3):
                block+=sudokuGrid[y][z]
        for z in range(8):
            number = block[z]                   
            if block.count(number)>1:          
                valid = False
            
    return valid
main()