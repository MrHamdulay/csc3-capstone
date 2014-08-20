'''A program that checks a soduku grid is valid or not
Jacob Ntesang
11 May 2014
'''
#Create an empty filled with zeros grid
grid = []
G2 = []
for i in range(9):
        row = input()
        for j in row:
                G2.append(j)
        grid.append(G2)
        G2 = []
#try to check if numbres in the same row are sme equivalent to one another
def check_equal_cells_in_a_row(grid):
        grid2 = []
        for i in range(9):
                for j in range(9):
                        if j < 8:
                                if grid[i][j] != grid[i][j+1]:
                                        if grid[i][j+1] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                                grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                                continue
                                        else:
                                                return False
                        elif j == 8:
                                if grid[i][j] not in  grid2:
                                        break
                                else:
                                        return False                     
                grid2 = []
        return True
#print(check_equal_cells_in_a_row(grid))
def check_equal_cells_in_a_col(grid):
        grid2 = []
        for i in range(9):
                for j in range(9):
                        if j < 8:
                                if grid[j][i] != grid[j+1][i]:
                                        if grid[j+1][i] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                                grid2.append(grid[j][i])#if a number is not equal to the next number ,add it to the list
                                                continue
                                
                                else:
                                        return False
                        elif j == 8:
                                if grid[j][i] not in  grid2:
                                        break
                                else:
                                        return False
                grid2 = []
        return True
#This function  checks if no 2 cells in the same 3x3 sub-grid have the same value - this is tested for the 9 non-overlapping sub-grids that a 9x9 grid can be divided into
#print(check_equal_cells_in_a_col(grid))
def check_equal_cells_in_3x3_sub_grids_1st(grid):
        grid2 = []
        for i in range(3):
                for j in range(3):
                        if grid[i][j] != grid[i][j+1]:
                                if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                        grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                        continue
                                else:
                                        #print(grid2)
                                        return False
                        else:
                                #print(grid2)
                                return False
        return True
#print(check_equal_cells_in_3x3_sub_grids_1st(grid))
def check_equal_cells_in_3x3_sub_grids_2nd(grid):
        grid2 = []
        for i in range(3):
                for j in range(3,6):
                        if grid[i][j] != grid[i][j+1]:
                                if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                        grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                        continue
                                else:
                                        #print(grid2)
                                        return False
                        else:
                                return False
        return True
#print(check_equal_cells_in_3x3_sub_grids_2nd(grid))
def check_equal_cells_in_3x3_sub_grids_3rd(grid):
        grid2 = []
        for i in range(3):
                for j in range(6,9):
                        if j != 8:
                                if grid[i][j] != grid[i][j+1]:
                                        if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                                grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                                continue
                                        else:
                                                return False
                                else:
                                        return False
        return True
#print(check_equal_cells_in_3x3_sub_grids_3rd(grid))
def check_equal_cells_in_3x3_sub_grids_4th(grid):
        grid2 = []
        for i in range(3,6):
                for j in range(3):
                        if grid[i][j] != grid[i][j+1]:
                                if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                        grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                        continue
                                else:
                                        return False
                        else:
                                return False
        return True
#print(check_equal_cells_in_3x3_sub_grids_4th(grid))
def check_equal_cells_in_3x3_sub_grids_5th(grid):
        grid2 = []
        for i in range(3,6):
                for j in range(3,6):
                        if grid[i][j] != grid[i][j+1]:
                                if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                        grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                        continue
                                else:
                                        return False
                        else:
                                return False
        return True
#print(check_equal_cells_in_3x3_sub_grids_5th(grid))
def check_equal_cells_in_3x3_sub_grids_6th(grid):
        grid2 = []
        for i in range(3,6):
                for j in range(6,9):
                        if j != 8:
                                if grid[i][j] != grid[i][j+1]:
                                        if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                                grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                                continue
                                        else:
                                                return False
                                else:
                                        return False
        return True
#print(check_equal_cells_in_3x3_sub_grids_6th(grid))
def check_equal_cells_in_3x3_sub_grids_7th(grid):
        N = 0
        grid2 = []
        for i in range(6,9):
                for j in range(3):
                        if grid[i][j] != grid[i][j+1]:
                                if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                        grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                        continue
                                else:
                                        return False
                        else:
                                return False
                                
        return True
#print(check_equal_cells_in_3x3_sub_grids_7th(grid))
def check_equal_cells_in_3x3_sub_grids_8th(grid):
        grid2 = []
        for i in range(6,9):
                for j in range(3,6):
                        if grid[i][j] != grid[i][j+1]:
                                if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                        grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                        continue
                                else:
                                        return False
                        else:
                                return False
        return True
#print(check_equal_cells_in_3x3_sub_grids_8th(grid))
def check_equal_cells_in_3x3_sub_grids_9th(grid):
        grid2 = []
        for i in range(6,9):
                for j in range(6,9):
                        if j != 8:
                                if grid[i][j] != grid[i][j+1]:
                                        if grid[i][j] not in  grid2:#Checks if a number is not equal to any number in a list,if not,return true
                                                grid2.append(grid[i][j])#if a number is not equal to the next number ,add it to the list
                                                continue
                                        else:
                                                return False
                                else:
                                        return False
        return True
if check_equal_cells_in_a_col(grid) and check_equal_cells_in_a_col(grid) and check_equal_cells_in_3x3_sub_grids_1st(grid) and check_equal_cells_in_3x3_sub_grids_2nd(grid) and check_equal_cells_in_3x3_sub_grids_3rd(grid) and check_equal_cells_in_3x3_sub_grids_4th(grid) and  check_equal_cells_in_3x3_sub_grids_5th(grid)and check_equal_cells_in_3x3_sub_grids_6th(grid) and check_equal_cells_in_3x3_sub_grids_7th(grid) and check_equal_cells_in_3x3_sub_grids_8th(grid) and check_equal_cells_in_3x3_sub_grids_9th(grid):
        print("Sudoku grid is valid")
else:
        print("Sudoku grid is not valid")
                
                        