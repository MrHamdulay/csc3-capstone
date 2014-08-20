"""Cherise Dube
14 May 2014
Program to check valid sudoku grid"""

#Takes the grid as an input
sudoku=""
for i in range(9):
    sudoku+=input()

#Create a 2-D array of sudoku numbers
grid_row=[]
for i in range(9):
    s=sudoku[i*9:(i*9)+9]
    s=s.replace(""," ")
    s=s.split(" ")
    s.remove("")
    s.remove("")
    s.sort()
    grid_row.append(s)
#Checks to see if 2 cells in same row are equal
valid1=True
for i in range(9):
    if valid1==True:
        pass
    else:
        break  
    for j in range(8):
        if grid_row[i][j]==grid_row[i][j+1]:
            valid1=False
            break
        else:
            continue


#Checks to see if two cells in the same column are equal
grid_column=[]
for j in range(9):
    s=""
    for i in range(j,81,9):
        s+=sudoku[i]
    s=s.replace(""," ")
    s=s.split(" ")
    s.remove("")
    s.remove("")
    s.sort()
    grid_column.append(s)

valid2=True
for i in range(9):
    if valid2==True:
        pass
    else:
        break
    for j in range(8):
        if grid_column[i][j]==grid_column[i][j+1]:
            valid2=False
            break
        else:
            continue
        
#Checks to see if two cells in the same region are equal
grid_region=[]
points=[0,3,6,27,30,33,54,57,60] #Points where each region starts
for i in points:
    s=""
    s+=sudoku[i:i+3]
    s+=sudoku[i+9:i+12]
    s+=sudoku[i+18:i+21]
    s=s.replace(""," ")
    s=s.split(" ")
    s.remove("")
    s.remove("")
    s.sort()
    grid_region.append(s)
    
valid3=True
for i in range(9):
    if valid3==True:
        pass
    else:
        break
    for j in range(8):
        if grid_region[i][j]==grid_region[i][j+1]:
            valid3=False
            break
        else:
            continue
        
if valid1==False or valid2==False or valid3==False:
    print("Sudoku grid is not valid")
    
else:
    print("Sudoku grid is valid")
    
        


    
    
    
    
        
    
        

        
            