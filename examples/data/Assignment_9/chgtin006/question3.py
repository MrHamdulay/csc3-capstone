#making a 2D array 
list1=[]
for i in range (9):
    sudoku=input("")
    list1.append([sudoku])
# checking if there is no repetion in row
def valid():
    print("Sudoku grid is valid")
def invalid():
    print("Sudoku grid is not valid")
def check_everything():
    test=[]
    for row in list1:
        for item in row:
            for col in item:
                if  not col in test:
                    test.append(col)
                else:
                    return invalid()
            

        test=[]
    
    
    test2=[]
    for i in range (9):
        for l in list1:
            for j in l:
                if not j[i] in test2:
                    test2.append(j[i])
                else:
                    return invalid()
        test2=[]
        return valid()
    
    
check_everything()
            

    
    
    