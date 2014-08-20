# Sudoku Validator

grid = []
i = 1
while i <= 9:
    x = input()
    i = i + 1
    grid.append(list(x))
    
trans = [[row[ind] for row in grid] for ind in range(len(grid[0]))]

sub1 = grid[0][:3] + grid[1][:3] + grid[2][:3]
sub2 = grid[0][3:6] + grid[1][3:6] + grid[2][3:6]
sub3 = grid[0][6:] + grid[1][6:] + grid[2][6:]
sub4 = grid[3][:3] + grid[4][:3] + grid[5][:3]
sub5 = grid[3][3:6] + grid[4][3:6] + grid[5][3:6]
sub6 = grid[3][6:] + grid[4][6:] + grid[5][6:]
sub7 = grid[6][:3] + grid[7][:3] + grid[8][:3]
sub8 = grid[6][3:6] + grid[7][3:6] + grid[8][3:6]
sub9 = grid[6][6:] + grid[7][6:] + grid[8][6:]

subgrid = [sub1, sub2, sub3, sub4, sub5, sub6, sub7,sub8, sub9]


for i in grid:
    if len(i) != len(set(i)):
        a = False
        break
    else:
        a = True
            
if a == True:
    for j in trans:
        if len(j) != len(set(j)):
            b = False
            break
        else:
            b = True
    if b == True:
        for k in subgrid:
            if len(k) != len(set(k)):
                c = False
                break
            else:
                c = True
        if c == False:
            print("Sudoku grid is not valid")
        else:
            print("Sudoku grid is valid")
            
    elif b == False:
        print("Sudoku grid is not valid")
        
elif a == False:
    print("Sudoku grid is not valid")
    

    
            
    
                
                










    

        
            





            
        

                

 
    
    
        

        


        
    


        

    
     
    
            