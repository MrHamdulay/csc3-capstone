def create_grid(grid):
    gri = ([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    for i in gri:
        grid.append(i)
    return grid

def print_grid (grid):
    fom = "{:<5}"
    print('+','-'*20,'+',sep='')
    
    for i in range(4):
        print('|',end='')
        for j in range(4):
            if grid[i][j] == 0:
                print('     ',end='')
            else:
                print(fom.format(grid[i][j]),end='',sep='')
        print('|')
    print('+','-'*20,'+',sep='')
    

def check_lost (grid):
    z = 0
    k = 0
    y = []
    f = []
    w = []
    t = []
    for yi in grid:
        y.append(yi[0])
    for fi in grid:
        f.append(fi[1])   
    for wi in grid:
        w.append(wi[2])       
    for ti in grid:
        t.append(ti[3])  
   # print(y,f,t,w)
    for i in grid:
        for j in range(3):
            if z not in i and i[j] != i[j+1] and y[j] == y[j+1]:
                return True
            else:
                return False
               # for j in range(4):
                #if y[j] == y[j+1]:
                    #return False
                #elif f[j] == f[j+1]:
                    #return False
                #elif w[j] == w[j+1]:
                    #return False
                #elif t[j] == t[j+1]:                
                    #return False
    #print(y)
def check_won (grid):
    z = 0
    k = 0
    for i in grid:
        for j in i:
            if j >= 32:
                return True
        else:
            return False
    
def copy_grid (grid):
    return grid

def grid_equal (grid1, grid2):
        j = 0
        for i in grid1:
            if i == grid2[j]:
                j += 1
                return True
    