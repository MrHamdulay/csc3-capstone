def soduku():
    
    grid=[]
    
    for i in range(9):
        string=input()
        row=[string[j] for j in range(9)]
        grid.append(row)
    
    for i in grid:
        for j in range(9):
            if i.count(i[j]) !=1:
                return "Sudoku grid is not valid"
    
    
    for i in range(9):
        
        grid2=[grid[j][i] for j in range(9)]
        
        for k in range(9):
            
            if grid2.count(grid2[k]) != 1:
                return "Sudoku grid is not valid"
                
    
    for i in range(9):
        for j in range(9):
            h1=0
            h2=2
            
            for x in range(3):
                
                if h1<=i<=h2 :
                    k1=0
                    k2=2
                    
                    for y in range(3):
                        
                        if k1<=j<=k2:
                            
                            subgrid=[grid[i][j] for i in range(h1,h2+1) for j in range(k1,k2+1)]
                            
                            for m in range(h1,h2+1):
                                    if subgrid.count(subgrid[m]) !=1:
                                        return "Sudoku grid is not valid"
                        k1+=3
                        k2+=3
                h1+=3
                h2+=3
    return "Sudoku grid is valid"                          
            
            
    
def main():
    print(soduku())
main()
