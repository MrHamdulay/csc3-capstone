#Thembekile Dubazana
#dbzphi002
#Assignment 9:Q3

"""Check if the sudoku grid is valid or not"""

#The input and variables
grid=[]
Sgrid=""

#Iterate fot the number of rows
for i in range(9):
        Sgrid+=input()
        
#Separate into 2D Array               
for j in range(0,82,9):
        List=[]
        List.append(Sgrid[j:j+9])
        grid.append(List)
        
#Remove the last empty list       
grid=grid[:-1]

#Separate string into individual items
for k in range(9):
        for l in range(9):
                grid[k].append(grid[k][0][l])
        grid[k]=grid[k][1:]

#Check for same value in row
def check_row(grid):
        for m in range(9):
                count=[]
                for n in range(9):
                        if grid[m][n] not in count:
                                count.append(grid[m][n])
                        else:
                                return False
        return sub_grid(grid)

#Check for same value in column
def check_column(grid):
        for o in range(9):
                count=[]
                for p in range(9):
                        if grid[p][o] not in count:
                                count.append(grid[p][o])
                        else:
                                return False
        return True
        


#Check the 3x3 sub grid for same values
def sub_grid(grid):
        for q in range(3):
                subgrid=grid[q:q+3]
                pos=0
                for t in range(3):
                        subgrid1=[]
                        for r in range(3):#loop over each 3 rows for 3 values
                                subgrid1.append(subgrid[r][t*3:(t*3)+3])
                        for s in range(9):#check for repetion of number
                                count=subgrid1.count(s)
                                if count > 1:
                                        return False
                        
        return check_column(grid)
                               

#The results
if check_row(grid)==True:
        print("Sudoku grid is valid")
else:
        print("Sudoku grid is not valid")

#Valid
259716483
867345912
413928675
398574126
546281739
172639548
984163257
621857394
735492861 

#Not valid
897243156
143765298
256981374
632897541
579416832
981352764
318674925
765129483
924538617        


  

           


