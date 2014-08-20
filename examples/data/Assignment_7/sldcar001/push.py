def push_up(grid):
    for row in range(4):
        add=[]
        for col in range(4):
            a=grid[col][row]
            if a!=0:
                add.append(a)
        g=0
        if len(add)!=0:
            while g < len(add):
                if g+1!=len(add):
                    if add[g]==add[g+1]:
                        add[g]=add[g]*2
                        del add[g+1]
                g+=1
        while len(add)!=4:
            add.append(0)
        for ncol in range(4):
            grid[ncol][row]=add[ncol]
    return(grid)

def push_down(grid):
    for row in range(4):
        add=[]
        for col in range(4):
            a=grid[col][row]
            if a!=0:
                add.append(a)
        add.reverse()
        g=0
        if len(add)!=0:
            while g < len(add):
                if g+1!=len(add):
                    if add[g]==add[g+1]:
                        add[g]=add[g]*2
                        del add[g+1]
                g+=1
        while len(add)!=4:
            add.append(0)
        add.reverse()
        for ncol in range(4):
            grid[ncol][row]=add[ncol]
    return(grid)
def push_left(grid):
    for row in range(4):
        add=[]
        for col in range(4):
            a=grid[row][col]
            if a!=0:
                add.append(a)
        g=0
        if len(add)!=0:
            while g < len(add):
                if g+1!=len(add):
                    if add[g]==add[g+1]:
                        add[g]=add[g]*2
                        del add[g+1]
                g+=1
        while len(add)!=4:
            add.append(0)
        for ncol in range(4):
            grid[row][ncol]=add[ncol]
    return(grid)

def push_right(grid):
    for row in range(4):
        add=[]
        for col in range(4):
            a=grid[row][col]
            if a!=0:
                add.append(a)
        add.reverse()
        g=0
        if len(add)!=0:
            while g < len(add):
                if g+1!=len(add):
                    if add[g]==add[g+1]:
                        add[g]=add[g]*2
                        del add[g+1]
                g+=1
        while len(add)!=4:
            add.append(0)
        add.reverse()
        for ncol in range(4):
            grid[row][ncol]=add[ncol]
    return(grid)
