#Shivam Ragoonaden - RGNSHI002
#13 May 2014
#Program to check validity of Sudoku grid

lines = []


for i in range (9):
    lines.append ([""] * 9)    #Create an empty 9x9 grid
  

for j in range(9):
    string  = input()  #Get line of Sudoku grid one by one from user
    for i in range(9):        
        lines[j][i] = string[i] #Assign the appropriate nunber from the line of input to the grid
        
bol = True  #Grid starts as valid by default


#Check the validity of the columns
for j in range (9):
    arr = []  #Temporary storage of values in each column
    for x in range (9):
        arr.append(lines[j][x])
    arr.sort()  #Sort it by numerical value
    
    for x in range (8):
        if arr[x] == arr[x+1]:  #Check if it is equal to the adjacent value
            bol = False  #Indicates that grid is false
            
#Check the validity of the rows  (Same as above but row and col switched around)
for y in range (9):
    arr = []  #Temporary storage of values in row
    for x in range (9):
        arr.append(lines[x][y])
    arr.sort()
             
    for x in range (8):
        if arr[x] == arr[x+1]:
            bol = False

#Checking each of the 9 3x3 Grids

for h in range(0,3,6): #Goes through the 3 different heights
    
    for w in range(0,3,6): #Goes through the 3 different widths
        
        arr_three = [] #Make it empty again for next iteration        
        
        #Adds all the values to a single array
        for j in range(3): 
            for i in range (3):        
                arr_three.append (lines[j][i+w])  #Adds all the digits in one 3x3 grid to a seperate array 
        arr_three.sort()  #Put in ascending order

        for x in range (8):
            if arr_three[x] == arr_three[x+1]:  #Test if there are any digits that match
                bol = False
        
if bol == False:  #Bol Test
    print("Sudoku grid is not valid")
else:
    print("Sudoku grid is valid")