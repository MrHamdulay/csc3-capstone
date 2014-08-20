'''f = open("sudoku_input","r")

full_list = []
for i in range(9):
    full_list.append(eval(f.readline()))
    
#print(full_list)'''


'''count = 0
for line in full_list:
    line_in_line = []    
    for digit in range(len(str(line))):
        line_in_line.append(str(line)[digit])
    line = line_in_line
    full_list[count] = line_in_line
    count += 1 '''
    
sudoku_list = []
for i in range(9):
    x = input()
    sudoku_list.append(x)
    
full_list = sudoku_list

sudoku_true = 0

# horizontal test
for j in range(len(full_list)):
    horizontal_list = full_list[j]
    check_list = []    
    for i in range(len(horizontal_list)):
        check_item = horizontal_list[i]
        if check_item in check_list:
            sudoku_true += 1
        check_list.append(check_item)
    
    #print(sudoku_true)

# make a vertical list

for col_no in range(len(full_list)):
    vertical_list = []
    for x in range(len(full_list)):
        vertical_item = full_list[x][col_no]
        vertical_list.append(vertical_item)
    
    for j in range(len(full_list)):
        check_list = []    
        for i in range(len(vertical_list)):
            check_item = vertical_list[i]
            if check_item in check_list:
                sudoku_true += 1
            check_list.append(check_item)
        
#print(vertical_list)
#print(full_list) 
# make a 3x3 list

for threerow in range(3):
    for threecol in range(3):
        threebythree = []    
        for row in range(3):    
            row = row + threerow*3            
            for col in range(3):
                mycol = col + threecol*3            
                threebythree.append(full_list[row][mycol])
    
        #print(threebythree)
        for j in range(len(full_list)):
            check_list = []    
            for i in range(len(threebythree)):
                check_item = threebythree[i]
                if check_item in check_list:
                    sudoku_true += 1
                check_list.append(check_item)

    
if sudoku_true == 0:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")

#f.close()