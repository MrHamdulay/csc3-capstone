"""sudoku grid checker
Joshua Hewitson
2/5/2014"""

#this function checks a set of 9 numbers and returns true if they are no repeats
def is_valid(list1):
    if len(set(list1)) == 9:
        return True
    else:
        return False

mylist = []
valid = True
sublist1 = []
# get input from user and list it in 9 lines
for i in range(9):
    sublist1.append(input())
sublist2 = []
sublist3 = []
# create 2d grid called mylist
for i in sublist1:
    mylist.append(list(i))
    
#check all horizontal lines:
for i in range(9):
    if not is_valid(mylist[i]):
        valid = False;
        break
    
#check all vertical lines:
for i in range(9):
    for j in range(9):
        sublist2.append(mylist[j][i])
    if not is_valid(sublist2):
        valid = False;
        break    

# check all 3x3 blocks
for i in range(0, 3, 3):
    for j in range(0, 3, 3):
        for k in range(3):
            for l in range(3):        
                sublist3.append(mylist[k + i][l + j])
        if not is_valid(sublist3):
            valid = False;
            i = 9
            j = 9
            break       
        
if valid:
    print("Sudoku grid is valid")
else:
    print("Sudoku grid is not valid")
        
    
        