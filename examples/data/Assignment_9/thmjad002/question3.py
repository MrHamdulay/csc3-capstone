"""Assignment 9, Question 3
Jadon Thomson
15-05-2014"""


def create_grid():
    """Creates a grid"""
    lst = []
    for repeate in range(9):
        lst.append(input())
    return lst

def check_horizontal(lst):
    """Check to see if there are any repetitions in rows of grid"""
    value = True
    for i in range(9):
        check = ''
        for j in lst[i]:
            if j in check:
                value = False
            else:
                check += str(j)
    return value

        
def check_vertical (lst):
    """check to see if there are any value repetitions in columns of grid"""
    value = True
    for i in range (9):
        check = ''
        for j in range (9):
            if lst[j][i] in check:
                value = False
            else:
                check += str(lst[j][i]) 
    return value

def check_cube(lst):
    """check to see if each block has more than one of each value""" 
    Col_Count = 0
    Row_Count = 0
    for Line1 in range(3): 
        check = [] 
        for i in range(Col_Count,Col_Count+3):  
            for j in range (Row_Count,Row_Count+3): 
                if lst[i][j] in check: 
                    return False
                else: 
                    check.append (lst[i][j])           
        Col_Count += 3
        check = []
    Col_Count = 0
    Row_Count = 3   
    for Line2 in range(3): 
        check = [] 
        for i in range (Col_Count,Col_Count+3): 
            for j in range (Row_Count,Row_Count+3): 
                if lst[i][j] in check: 
                    return False
                else:     
                    check.append (lst[i][j])                 
        Col_Count += 3
        check = []        
    Col_Count = 0    
    Row_Count = 6
    for Line3 in range (3): 
        check = [] 
        for i in range (Col_Count,Col_Count+3): 
            for j in range (Row_Count,Row_Count+3): 
                if lst[i][j] in check: 
                    return False
                else:     
                    check.append(lst[i][j])                 
        Col_Count += 3
        check = [] 
    return True    
    
def main():
    """controls the program"""
    a = create_grid()
    if check_cube(a) and check_vertical(a) and check_horizontal(a):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
        
main()