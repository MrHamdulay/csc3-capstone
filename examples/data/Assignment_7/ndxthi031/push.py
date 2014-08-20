#Thiolan Prevan Naidoo
#NDXTHI031
#question3 

def Mzero(a):
    for i in range(1,4):
        x=i
        while a[x-1]==0 and x>0:#moves a number towards the start of the list if there is a zero before it
            a[x-1]=a[x]
            a[x]=0
            x=x-1

def operate(a):#the function that each push function will call. it recieves a 4 item list as a parameter
    for j in range(4):
        if type(a[j])==type("b"):#changes each string value in the lst to a zero
            a[j]=0      
            
    Mzero(a)
            
    for i in range(3):#multiplies a number by two in the list if the adjacent number is the same and sets the second number to zero
        if a[i]==a[i+1]:
            a[i]=2*a[i]
            a[i+1]=0
            
    Mzero(a)

def push_up(grid):#slide up function in the game
    for x in range(4):
        a=[grid[0][x],grid[1][x],grid[2][x],grid[3][x]]#takes out each column separately and sends it as a parameter the the function operate
        operate(a)
        for i in range(4):#assigns each value in a specific column to the corresponding values that have been returned by operate n the list a
            grid[i][x]=a[i]
            
def push_down(grid):#slide down function in the game
    for x in range(4):
        a=[grid[3][x],grid[2][x],grid[1][x],grid[0][x]]#pulls out the column in reverse so that operate recieves a uniform list all the time
        operate(a)
        a.reverse()#reverses list a so that the zeroes added by operate are at the top of the grid
        for i in range(4):
            grid[i][x]=a[i]    

def push_left(grid):#slide left function in the game
    for x in range(4):
        a=[grid[x][0],grid[x][1],grid[x][2],grid[x][3]]#takes out each row separately and sends it as a parameter the the function operate
        operate(a)
        
        for i in range(4):
            grid[x][i]=a[i]      
            
def push_right(grid):#slide right function in the game
    for x in range(4):
        a=[grid[x][3],grid[x][2],grid[x][1],grid[x][0]]#pulls out the row in reverse so that operate always recieves a uniform list.
        operate(a)
        a.reverse()#reverses list a so that the zeroes added by operate are to the right of the grid.
        for i in range(4):
            grid[x][i]=a[i]   