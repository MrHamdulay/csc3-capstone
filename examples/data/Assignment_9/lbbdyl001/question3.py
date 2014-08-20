""" Sudoku validity checker
Dylan Lubbe
16 May 2014"""

line = ""
grid = []
lines = []
final_counter = 0
def s_grid ():
    lines = []
    for i in range (9):
        line = input ()
        for j in line:
            lines.append (j)
        grid.append (lines)
        lines = []

def row_check (grid):
    empty = []
    counter = 0
    for i in range (9):
        for num in grid[i]:
            if num not in empty:
                empty.append(num)
        if len(empty) == 9:
            counter += 1
            empty = []
    if counter == 9:
        global final_counter
        final_counter += 1
        
def col_check (grid):
    col = []
    counter = 0
    for i in range (9):
        for j in range (9):
            if grid[j][i] not in col:
                col.append (grid[j][i])
        if len(col) == 9:
            counter += 1
            col = []
    if counter == 9:
        global final_counter 
        final_counter += 1
            
boxes = []
box = []
def box_create (grid):
    box = []
    for i in range (3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    box.append (grid[k+(i*3)][l+(j*3)])
            boxes.append (box)
            box = []

def box_check (boxes):
    empty = []
    counter = 0
    for i in range (9):
        for j in boxes[i]:
            if j not in empty:
                empty.append (j)
        if len(empty) == 9:
            counter += 1
            empty = []
    if counter == 9:
        global final_counter 
        final_counter += 1
        
                       
s_grid()
row_check(grid)
col_check(grid)
box_create(grid)
box_check(boxes)
if final_counter == 3:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
    

    
    
            
        
        
        