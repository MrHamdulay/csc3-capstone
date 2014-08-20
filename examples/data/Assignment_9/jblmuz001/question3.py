"""Assignment 9 Question 2
Muzammil Jable
14 May 2014"""

def check(grid):
    """checks to see if the grid is valid or not"""
    for row in grid:
        for i in range(1, 10):
            if row.count(i)!=1:
                return False
    return True


def column(grid):
    """divides a given grid down the columns rather than rows"""
    new_grid=[]
    a,b,c,d,e,f,g,h,k=[],[],[],[],[],[],[],[],[]
    for i in range(9):
        a.append(grid[i][0])
    for i in range(9):
        b.append(grid[i][1])
    for i in range(9):
        c.append(grid[i][2])
    for i in range(9):
        d.append(grid[i][3])
    for i in range(9):
        e.append(grid[i][4])
    for i in range(9):
        f.append(grid[i][5])
    for i in range(9):
        g.append(grid[i][6])
    for i in range(9):
        h.append(grid[i][7])
    for i in range(9):
        k.append(grid[i][8])
    new_grid.append(a)
    new_grid.append(b)
    new_grid.append(c)
    new_grid.append(d)
    new_grid.append(e)
    new_grid.append(f)
    new_grid.append(g)
    new_grid.append(h)
    new_grid.append(k)
    return new_grid
    
def sub_grid(grid):
    """divides a given array into 9 non-overlapping subgrids"""
    new_grid=[]
    a,b,c,d,e,f,g,h,k=[],[],[],[],[],[],[],[],[]
    for i in range(3):
        for j in range(3):
            a.append(grid[i][j])
    for i in range(3):
        for j in range(3, 6):
            b.append(grid[i][j])
    for i in range(3):
        for j in range(6, 9):
            c.append(grid[i][j])
    for i in range(3,6):
        for j in range(3):
            d.append(grid[i][j])
    for i in range(3,6):
        for j in range(3, 6):
            e.append(grid[i][j])
    for i in range(3,6):
        for j in range(6, 9):
            f.append(grid[i][j])
    for i in range(6, 9):
        for j in range(3):
            g.append(grid[i][j])
    for i in range(6, 9):
        for j in range(3, 6):
            h.append(grid[i][j])
    for i in range(6, 9):
        for j in range(6, 9):
            k.append(grid[i][j]) 
    new_grid.append(a)
    new_grid.append(b)
    new_grid.append(c)
    new_grid.append(d)
    new_grid.append(e)
    new_grid.append(f)
    new_grid.append(g)
    new_grid.append(h)
    new_grid.append(k)
    return new_grid

def grided(string):
    """a very ugly function to turn the string input into a 2D array"""
    grid=[]
    x,y,z,r,t,u,o,p,q=[],[],[],[],[],[],[],[],[]
    a,b,c,d,e,f,g,h,k=[string[:9]],[string[9:18]],[string[18:27]],[string[27:36]],[string[36:45]],[string[45:54]],[string[54:63]],[string[63:72]],[string[72:81]]
    for i in a:
        for j in i:
            x.append(eval(j))
    for i in b:
        for j in i:
            y.append(eval(j))
    for i in c:
        for j in i:
            z.append(eval(j))
    for i in d:
        for j in i:
            r.append(eval(j))
    for i in e:
        for j in i:
            t.append(eval(j))
    for i in f:
        for j in i:
            u.append(eval(j))
    for i in g:
        for j in i:
            o.append(eval(j))
    for i in h:
        for j in i:
            p.append(eval(j))
    for i in k:
        for j in i:
            q.append(eval(j))
    grid.append(x)
    grid.append(y)
    grid.append(z)
    grid.append(r)
    grid.append(t)
    grid.append(u)
    grid.append(o)
    grid.append(p)
    grid.append(q)
    return grid
    

def main():
    """function to request input from users and print out the validity of the input sudoku grid"""
    a,b,c,d,e,f,g,h,i=input(),input(),input(),input(),input(),input(),input(),input(),input()
    x=a+b+c+d+e+f+g+h+i    
    grid=grided(x)
    row=check(grid)
    col=column(grid)
    cool=check(col)
    lil_grid=sub_grid(grid)
    gridlings=check(lil_grid)
    
    if cool and row and gridlings:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

main()