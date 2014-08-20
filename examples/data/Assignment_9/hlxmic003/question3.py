# Michaela Heale
# Assignment 9 Question 3


def main():
    grid = []
    for z in range(0,9):
        oneline=[] #added as was not defined
        line = input()
        for blue in line:
                oneline.append(blue)
        grid.append(oneline)
    graph = checker(grid)
    
    if graph:
        print("Sudoku grid is valid")
    else:
        print("Sudoku grid is not valid")

def checker(array):
    z=0
    a=0
    for mice in range(9):
        z=0
        for rice in range(9):
            z+= eval(array[mice][rice])
            if z==45:
                a+=1
    if a !=9:
        return False  
    else:
        a=0
        for hen in range(9):
                z=0
                for egg in range(9):
                    z+= eval(array[egg][hen])
                    if z==45:
                        a+=1
        if a !=9:
            return False    
        else:
            a=0
            for cat in range(3):
                
                            z=0
                            for dog in range(3):
                                z+= eval(array[dog][cat])
                            a+=z
            if a!=45:
                return False
                
            else:
                return True
                

        
main()

