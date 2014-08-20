def sudoku_checker():
    grid=[]
    grid3=[]
    thr=range(3)
    ip=0
    while ip<9:
        game=list(input())
        grid.append(game)
        ip+=1
    bb=0
    be=3
    three=[]
    while be<=9:
        for row in range(9):
            for col in range(bb,be):
                n=grid[row][col]
                three.append(n)
            if row==2 or row==5 or row==8:
                grid3.append(three)
                three=[]
            if row+1==9:
                bb+=3
                be+=3
    valid="Yep"
    for row in range(9):
        for col in range(9):
            a=grid[row][col]
            for i in range(9):
                b=grid[row][i]
                c=grid[i][col]
                if a==b and i!=col:
                    valid="Nop"
                    return(valid)
                if a==c and i!=row:
                    valid="Nop"
                    return(valid)      
    for row in range(9):
        for col in range(9):
            s=grid3[row][col]
            for i in range(9):
                j=grid3[row][i]
                if s==j and i!=col:
                    valid="Nop"
                    return(valid)
    return(valid)
def main():
    a=sudoku_checker()
    if a=="Yep":
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")
main()