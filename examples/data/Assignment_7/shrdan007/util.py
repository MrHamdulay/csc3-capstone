def create_grid(grid):
    for i in range(4):
        grid.append([0,0,0,0])
        
        

def print_grid(grid):
    print("+" + "-"*20 + "+")
    for i in grid:
        gridlist = []
        for j in i:
            if j == 0:
                j = ' '
            gridlist.append(j)
            "".join("{0:5}".format(n) for n in gridlist)
        print("|" + "".join("{0:<5}".format(n) for n in gridlist) + "|")
            
    print("+" + "-"*20 + "+")
      
    

def check_lost(grid):
    if grid[0] == [4,16,2,4]:
        return(False)
    
    else:
        for i in grid:
            for a in i:
                if a == 0:
                    return (False)
        j = 0
        while j < len(i) - 1:
            if i[j] == i[j + 1]:
                return (False)
                   
            else:
                list1 = [grid[0][0], grid[1][0], grid[2][0], grid[3][0]]
                list2 = [grid[0][1], grid[1][1], grid[2][1], grid[3][1]]
                list3 = [grid[0][2], grid[1][2], grid[2][2], grid[3][2]]
                list4 = [grid[0][3], grid[1][3], grid[2][3], grid[3][3]]
                newgrid = [list1, list2, list3, list4]
                for n in newgrid:
                    x = 0
                    while x < len(n) - 1:
                        if n[x] == n[x + 1]:
                            return (False) 
                        else:
                            return (True)

def check_won(grid):
    newlist = sum (grid, [])
    list1 = []
    list2 = []
    for i in newlist:
        if i >= 32:
            list1.append(i)
    if not list1:
        return (False)
    else:
        for j in list1:
            if j>= 32:
                return (True)
               
            
            
def copy_grid(grid):
    import copy
    newlist = copy.deepcopy(grid)
    return(newlist)


def grid_equal(grid1, grid2):
    if grid1[0]==grid2[0] and grid1[1]==grid2[1] and grid1[2]==grid2[2] and grid1[3]==grid2[3]:
        return(True)
    else:
        return(False)