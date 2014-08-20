'''Name: Yongama Giwu
Question 3 Assignment 9'''

listofnum=[]

for i in range(9):
    numbers=input()
    listofnum.append(numbers)




def create_grid():
    grid=[]
    """create a 9x9 grid"""
    height = 9
    for i in range (height):
        grid.append ([0] * 9)
    return grid
grid=create_grid()

#assign values to grid
for i in range(9):
    for j in range(9):
        grid[i][j]=listofnum[i][j]

def check_columns(grid):
    column_list=[]
    for row in range(9):
        del column_list
        column_list=[]
        for column in range(9):
            if grid[column][row] not in column_list:
                column_list.append(grid[column][row])
        if len(column_list)<9:
            return False
            break
    else:
        return True


def check_rows(grid):
    row_list=[]
    for column in range(9):
        del row_list
        row_list=[]
        for row in range(9):
            if grid[column][row] not in row_list:
                row_list.append(grid[column][row])
        if len(row_list)<9:
            return False
            break
    else:
        return True
prime=True
def check_boxes(grid):
    smaller_grid=[]
    global prime
    for column in range(0,9,3):
        for i in range(0,9,3):
            del smaller_grid
            smaller_grid=[]
            for row in range(i,i+3):
                smaller_grid.append(grid[row][column:column+3])


            checklist=[]
            for x in range(3):
                for y in range(3):
                    if smaller_grid[x][y] not in checklist:
                        checklist.append(smaller_grid[x][y])

            if len(checklist)<9:
                prime=False
    return prime






def main(grid):
    if check_boxes(grid) and check_columns(grid) and check_rows(grid):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
main(grid)



