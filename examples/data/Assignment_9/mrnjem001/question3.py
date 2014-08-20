def get_grid():
    x=input("")
    grid=[]
    count=0
    while count<9:
        subgrid=[]
        for i in x:
            subgrid.append(i)
        grid.append(subgrid)
        count+=1
        if count!=9:
            x=input("")
    return grid
    
def check_valid(grid):
    stop=0
    for i in range(9):
        for j in range(1,10):
            if grid[i].count(str(j))!=1:
                stop=1
                break
        
        else:
            continue  # executed if the loop ended normally (no break)
        break  # executed if 'continue' was skipped (break)       

    if stop!=1:
        for i in range(9):
            tempgrid=[]
            for j in range(9):
                tempgrid.append(grid[j][i])
            for h in range(1,10):
                if tempgrid.count(str(h))!=1:
                    stop=1
                    break
            else:
                continue  # executed if the loop ended normally (no break)
            break  # executed if 'continue' was skipped (break)            
            
    if stop!=1:
        for rows in range(0,3):
            for hstar in range(0,3):
                tempgrid2=[]        
                for i in range(3*rows,3*rows+3):
                    tempgrid=[]
                    for h in range(3*hstar,3*hstar+3):            
                        tempgrid.append(grid[i][h])
                    tempgrid2.append(tempgrid)
                tempgrid3=[]
                for row in range(3):
                    for col in range(3):
                        tempgrid3.append(tempgrid2[row][col])
                for h in range(1,10):
                    if tempgrid3.count(str(h))!=1:
                        stop=1          
                        break
    if stop==0:
        print("Sudoku grid is valid")
    elif stop==1:
        print("Sudoku grid is not valid")


check_valid(get_grid())
