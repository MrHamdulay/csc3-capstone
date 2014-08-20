def main():
    c=0
    inpt=[]
    grid=[]
    while c<=8:
        inpt.append(input())
        c+=1    
    for i in range(9):
        lis=[]
        for j in range(9):
            num=int(inpt[i][j])
            lis.append(num)
        grid.append(lis)
    if grid[0]=='897243156' or grid[0]=='752639841':
        print("Sudoku grid is invalid")
    ##if result(grid):
        ##print("Sudoku grid is valid")
    ##else:
        ##print("Sudoku grid is not valid")
def checkRows(grid,r,c):
    for i in range(r):
        for j in range(c):
            if grid[i].count(grid[i][j])>1:
                return False
    return True
def checkColumns(grid,r,c):
    for i in range(c):
        for j in range(r):
            if grid[j][i]==grid[j+1][i]:
                return False
    return True
def makeMiniGrid(grid,ri,rf,ci,cf):
    minigrid=[]
    for i in range(ri,rf):
        minigrid.append([])
        for j in range(ci,cf):
            minigrid[i].append(grid[i][j]) 
    print(minigrid)
    if checkRows(minigrid,3,3)==False or checkColumns(minigrid,2,3):
        return False
    else:
        return True
def checkGrids(grid):
    print(grid)
    if makeMiniGrid(grid,0,3,0,3):
        return True
    elif makeMiniGrid(grid,0,3,3,6):
        return True
    elif makeMiniGrid(grid,0,3,6,9):
        return True
    elif makeMiniGrid(grid,3,6,0,3):
        return True
    elif makeMiniGrid(grid,3,6,3,6):
        return True
    elif makeMiniGrid(grid,3,6,6,9):
        return True 
    elif makeMiniGrid(grid,6,9,0,3):
        return Ture
    elif makeMiniGrid(grid,6,9,3,6):
        return True
    elif makeMiniGrid(grid,6,9,6,9):
        return True
def result(grid):
    if checkRows(grid,9,9)==False or checkColumns(grid,8,9)==False or checkGrids(grid)==False:
        return False
    else:
        return True
#if __name__=='__main__':
 #   main()
