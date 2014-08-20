#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014-05-13
#Function       : Checks if a sudoku solutions valid
#Title          : Question


def check_extract(extracted_list):
    for number in range(1, 10):
        if extracted_list.count(number) != 1:
            return False
    return True


def test(sudoku):
    """test if a sudoku solution is valid"""
    #horizontal test
    for horizontal in sudoku:
        #Extracts a horizontal component of the grid tests it
        if not check_extract(horizontal):
            return False
    #verticle test
    for vertical in range(9):
        #shifts the column number
        extracted_list = []
        for horizontal in sudoku:
            #Extracts a vertical column of the list and tests it
            extracted_list.append(horizontal[vertical])
        if not check_extract(extracted_list):
            return False
    extracted_list = []

    #3*3 grid test
    #Splits the grid into 3*3 section and iterates over the 9 sections
    for x_block in range(0, 9, 3):
        for y_block in range(0, 9, 3):
            #puts each value in a 3*3 section into a list
            for x in range(x_block, x_block+3):
                for y in range(y_block, y_block+3):
                    extracted_list.append(sudoku[y][x])
            #test the extracted
            if not check_extract(extracted_list):
                return False
            extracted_list = []

    return True


sudoku = []
for i in range(9):
    #takes each value in a string of numbers and adds them to a list as an int
    line = list(map(int, input()))
    #adds each list of integers in a 2D list
    sudoku.append(line)

if test(sudoku):
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")



