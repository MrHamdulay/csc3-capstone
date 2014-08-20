grid=[]
def create_grid(grid):
    
    #grid=[]
    for a in range(4):
        grid.append([" "]*4)    
                   
def print_grid(grid):
    style="{" ":<5}"
    print("+","-"*20,"+",sep="")
    
    for y in range(4):
        print("|",end="")
        for x in range(4):
            print(style.format(grid[y][x]),end="")
        print("|")
    print("+","-"*20,"+",sep="")

TorF=[]
def check_lost(grid):
    #check if there is a 0 in the grid
    for y in grid:
        if " " in y :
            answer=0
            TorF.append(answer)
    
    #check if any adjascent numbers are the same     
    for y in range(4):
        for x in range(4):
            if x>0:
                if grid[y][x]==grid[y][x-1]:
                    answer=0
                    TorF.append(answer)
            if x<3:
                if grid[y][x]==grid[y][x+1]:
                    answer=0
                    TorF.append(answer)
            if y>0:
                if grid[y][x]==grid[y-1][x]:
                    answer=0
                    TorF.append(answer)
            if y<3:
                if grid[y][x]==grid[y+1][x]:
                    answer=0
                    TorF.append(answer)
    if 0 in TorF:
        return False
    else:
        return True

wincheck=[]
def check_won(grid):
    for y in grid:
        for x in y:
            if x>=32:
                check="T"
                wincheck.append(check)
    if "T" in check:
        return True
    else:
        return False
    
def copy_grid(grid):
    new=grid
    
equal=[]
def grid_equal(grid,new):
    for y in range(4):
        for x in range(4):
            if grid[y][x]!=new[y][x]:
                equal.append("F")
    if "F" in equal:
        return False
    else:
        return True
    
            
