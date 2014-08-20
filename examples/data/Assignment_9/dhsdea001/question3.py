#Question 3
#Soduku checker
#By: Dean de Haast

unique= True
three_array= []
lines = []
temp =[]
#Creating the array
for i in range (9):
    lines.append ([""] * 9)     

#Writing the grid to an array
for y in range(9):
    string  = input()
    for i in range(9):        
        lines[y][i] = string[i]

#Checking Columns
for y in range (9):
    temp=[]
    for x in range (9):
        temp.append(lines[y][x])
    temp.sort()
    
    for x in range (8):
        if temp[x]==temp[x+1]:
            unique = False
            
#Checking Rows
for y in range (9):
    temp=[]
    for x in range (9):
        temp.append(lines[x][y])
    temp.sort()
             
    for x in range (8):
        if temp[x]==temp[x+1]:
            unique = False

#Checking 3x3 Grids
for h in range(0,3,6): #Goes through the 3 different heights
    for k in range(0,3,6): #Goes through the 3 different widths
        #Adds all the values to a single array
        for y in range(3): 
            for i in range (3):        
                three_array.append (lines[y][i+k])
        three_array.sort()

        for x in range (8):
            if three_array[x]==three_array[x+1]:
                unique = False
        three_array =[]

three_array.append
        
if unique == False:
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")