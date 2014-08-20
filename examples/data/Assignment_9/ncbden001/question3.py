'''Program to check validity of Sudoku grids
   Denzel Ncube
   05 May 2014'''


#Grids for each line and big grid
mastergrid = []
grid1 =[]
grid2 = []
grid3 = []
grid4 =[]
grid5 =[]
grid6 = []
grid7 = []
grid8 = []
grid9 = []

subgrid1 =[]
subgrid2 = []
subgrid3 = []
subgrid4 =[]
subgrid5 =[]
subgrid6 = []
subgrid7 = []
subgrid8 = []
subgrid9 = []


inp = ''
#Function to split the input 
def splitter(string):
    split = ''
    lst = []
    for i in range(9):
        lst.append(string[i])   
    return lst
       
#putting input into grids and subgrids
grid1 = splitter(input())
grid2 = splitter(input())    
grid3 = splitter(input())
grid4 = splitter(input())        
grid5 = splitter(input())        
grid6 = splitter(input())
grid7 = splitter(input())
grid8 = splitter(input())
grid9 = splitter(input())

for i in range(0,3):
    subgrid1.append(grid1[i])
    subgrid1.append(grid2[i])
    subgrid1.append(grid3[i])


for i in range(3,6):
    subgrid2.append(grid1[i])
    subgrid2.append(grid2[i])
    subgrid2.append(grid3[i])


for i in range(6,9):
    subgrid3.append(grid1[i])
    subgrid3.append(grid2[i])
    subgrid3.append(grid3[i])


for i in range(0,3):
    subgrid4.append(grid4[i])
    subgrid4.append(grid5[i])
    subgrid4.append(grid6[i])

for i in range(3,6):
    subgrid5.append(grid4[i])
    subgrid5.append(grid5[i])
    subgrid5.append(grid6[i])


for i in range(6,9):
    subgrid6.append(grid4[i])
    subgrid6.append(grid5[i])
    subgrid6.append(grid6[i])


for i in range(0,3):
    subgrid7.append(grid7[i])
    subgrid7.append(grid8[i])
    subgrid7.append(grid9[i])


for i in range(3,6):
    subgrid8.append(grid7[i])
    subgrid8.append(grid8[i])
    subgrid8.append(grid9[i])


for i in range(6,9):
    subgrid9.append(grid7[i])
    subgrid9.append(grid8[i])
    subgrid9.append(grid9[i])


#Putting grids into mastergrid
mastergrid = [grid1,grid2,grid3,grid4,grid5,grid6,grid7,grid8,grid9]  

#Checking if game is won
result = ''

#Checking rows
grid1.sort() 
grid2.sort()  
grid3.sort() 
grid4.sort() 
grid5.sort()        
grid6.sort() 
grid7.sort() 
grid8.sort() 
grid9.sort() 
            
for i in range(0,8):
            if grid1[i] == grid1[i+1] or grid2[i]==grid2[i+1] or grid3[i]==grid3[i+1] or grid4[i]==grid4[i+1] or grid5[i]==grid5[i+1] or grid6[i]==grid6[i+1] or grid7[i]==grid7[i+1] or grid8[i]==grid8[i+1] or grid9[i]==grid9[i+1]:
                result += 'false'
                


#Checking sub-grids
subgrid1.sort() 
subgrid2.sort()  
subgrid3.sort() 
subgrid4.sort() 
subgrid5.sort()        
subgrid6.sort() 
subgrid7.sort() 
subgrid8.sort() 
subgrid9.sort() 

for i in range(0,8):
    if subgrid1[i] == subgrid1[i+1] or subgrid2[i]== subgrid2[i+1] or subgrid3[i]== subgrid3[i+1] or subgrid4[i]== subgrid4[i+1] or subgrid5[i]== subgrid5[i+1] or subgrid6[i]== subgrid6[i+1] or subgrid7[i]== subgrid7[i+1] or subgrid8[i]== subgrid8[i+1] or subgrid9[i]== subgrid9[i+1]:
        result += 'false'
#Displaying appropriate output
if 'false' in result:
    print("Sudoku grid is not valid")
else:   
    print("Sudoku grid is valid")