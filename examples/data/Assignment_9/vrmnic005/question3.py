#vrmnic005
#assignment 9, question 3

box_corners = [(0, 0), (0, 3), (0, 6),
               (3, 0), (3, 3), (3, 6),
               (6, 0), (6, 3), (6, 6)]
box_diffs = [(0, 0), (0, 1), (0, 2),
             (1, 0), (1, 1), (1, 2),
             (2, 0), (2, 1), (2, 2)]

def check_sudoku(puzzle):
    # check rows
    for row in puzzle:
        if len(set(row)) != 9:
            return False

    #check columns
    for col in range(9):
        if len(set([row[col] for row in puzzle])) != 9:
            return False

    #check 3x3 squares
    for row, col in box_corners:
        if len(set([puzzle[row+row_diff][col+col_diff] for row_diff, col_diff in box_diffs])) != 9:
            return False

    return True

puzzle = []
for i in range(9):
    x = input()
    puzzle.append(list(map(int, x)))

if check_sudoku(puzzle) == True:
    print("Sudoku grid is valid")

else:
    print("Sudoku grid is not valid")