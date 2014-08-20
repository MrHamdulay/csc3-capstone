
#Create a 2D array from users input
grid=[]
grid2=[]
for i in range(9):
    row=input()
    for i in row:
        grid2.append(i)
    #row=row.split()
    grid.append(grid2)
    grid2=[]



#Iterate through array and check follg cases:
k=True
for row in range(9):
    for col in range(9):
        if col==0:
            if grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row][col+2] or grid[row][col]==grid[row][col+3] or grid[row][col]==grid[row][col+4] or grid[row][col]==grid[row][col+5] or grid[row][col]==grid[row][col+6] or grid[row][col]==grid[row][col+7] or grid[row][col]==grid[row][col+8]:
                k=False
                
        if row==0:
            if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row+2][col] or grid[row][col]==grid[row+3][col] or grid[row][col]==grid[row+4][col] or grid[row][col]==grid[row+5][col] or grid[row][col]==grid[row+6][col] or grid[row][col]==grid[row+7][col] or grid[row][col]==grid[row+8][col]:
                k=False
                
        if col==0 or col==3 or col==6:
            if row == 0 or row==3 or row==6:
                if grid[row][col]==grid[row+1][col] or grid[row][col]==grid[row+2][col] or grid[row][col]==grid[row][col+1] or grid[row][col]==grid[row][col+2] or grid[row][col]==grid[row+1][col+1] or grid[row][col]==grid[row+1][col+2] or grid[row][col]==grid[row+2][col+1] or grid[row][col]==grid[row+2][col+2]:
                    k=False
            
            
                if grid[row+1][col]==grid[row+2][col] or grid[row+1][col]==grid[row][col+1] or grid[row+1][col]==grid[row][col+2] or grid[row+1][col]==grid[row+1][col+1] or grid[row+1][col]==grid[row+1][col+2] or grid[row+1][col]==grid[row+2][col+1] or grid[row+1][col]==grid[row+2][col+2]:
                    k=False            
        
            
                if grid[row+2][col]==grid[row][col+1] or grid[row+2][col]==grid[row][col+2] or grid[row+2][col]==grid[row+1][col+1] or grid[row+2][col]==grid[row+1][col+2] or grid[row+2][col]==grid[row+2][col+1] or grid[row+2][col]==grid[row+2][col+2]:
                    k=False 
                    
                if grid[row][col+1]==grid[row+1][col+1] or grid[row][col+1]==grid[row+1][col+2] or grid[row][col+1]==grid[row+2][col+1] or grid[row][col+1]==grid[row+2][col+2] or grid[row][col+1]==grid[row+1][col+2]:
                    k=False 
                    
                if grid[row+1][col+1]==grid[row][col+2] or grid[row+1][col+1]==grid[row+2][col+1] or grid[row+1][col+1]==grid[row+1][col+2] or grid[row+1][col+1]==grid[row+2][col+2]:
                    k=False 
                    
                if grid[row+2][col+1]==grid[row][col+2] or grid[row+2][col+1]==grid[row+1][col+2] or grid[row+2][col+1]==grid[row+2][col+2]:
                    k=False
                    
                if grid[row][col+2]==grid[row+1][col+2] or grid[row][col+2]==grid[row+2][col+2] :
                    k=False
                    
                if grid[row+1][col+2]==grid[row+2][col+2]:
                    k=False
                
        
        
        


if k==True:
    print("Sudoku grid is valid")

if k==False:
    print("Sudoku grid is not valid")