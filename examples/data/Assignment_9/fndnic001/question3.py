'''check if a soduku grid is valid or not
nic findlay
13 may 2013'''

def grid(): # get sudoku as 2d list
    string_sudoku=[]
    list_sudoku=[]
    
    grid1 = []
    row = 0
        
    for i in range(9):  #makes one long list of all values in sudoku
        row=input("")
        list_sudoku.append(row)
        for i in range(9):
            string_sudoku.append(row[i])
    
    for i in range(0,len(string_sudoku),9):  #takes long list and transforms into 2d
        grid1.append(string_sudoku[i:i+9])
    return grid1

def check_row(grid1):
    var = True
    combo = []
    for row in range(len(grid1)):
        for col in range(len(grid1)):
            if grid1[row][col] in combo:
                var = False
            else:
                combo.append(grid1[row][col])
        combo = []
    return var

def check_column(grid1):
    var = True
    combo = []
    for col in range(len(grid1)):
        for row in range(len(grid1)):
            if grid1[row][col] in combo:
                var = False
            else:
                combo.append(grid1[row][col])
        combo = []
    return var

def check_box(grid1):
    #determine what box a item is in
    #     1 2 3
    #     4 5 6
    #     7 8 9
    var = True
    box1 = []
    box2 = []
    box3 = []
    box4 = []
    box5 = []
    box6 = []
    box7 = []
    box8 = [] 
    box9 = []
    for row in range(len(grid1)):
            for col in range(len(grid1)):        
                if row<4 and col<4:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box1.append(grid1[row][col])
                elif row<4 and col<7:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box2.append(grid1[row][col])                    
                elif row<4 and col<10:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box3.append(grid1[row][col])                    
                elif row<7 and col<4:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box4.append(grid1[row][col])                    
                elif row<7 and col<7:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box5.append(grid1[row][col])                    
                elif row<7 and col<10:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box6.append(grid1[row][col])                    
                elif row<10 and col<4:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box7.append(grid1[row][col])                    
                elif row<10 and col<7:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box8.append(grid1[row][col])                    
                elif row<10 and col<10:
                    if grid1[row][col] in box1:
                        var = False
                    else:
                        box9.append(grid1[row][col])                    
    return var  


def main():
    grid1 = grid()
    if check_row(grid1) and check_column(grid1): #and check_box(grid1):
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
main()
grid1 = [['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9'], ['1','2','3','4','5','6','7','8','9']]
