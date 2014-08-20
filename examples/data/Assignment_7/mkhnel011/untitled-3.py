def print_grid(grid):
    height = 4
    grid = [[4,2,8,2],[2,8,16,8],[16,32,8,4],[4,8,4,2]]
    print("+","-"*20,"+",sep="")
    for row in range (height):
        print("|",end="")
        for col in range (height):
            print ("{0:<5}".format(grid[row][col]), end="")
        print("|",end="")
        print ()
    print("+","-"*20,"+",sep="")
print_grid([[4,2,8,2],[2,2,16,8],[16,32,8,4],[4,8,4,2]])