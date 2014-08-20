"""Saijil Nemchund
NMCSAI001
Program that creates the 2048 game"""

def basic(a):  
    for j in range(4):
        if type(a[j])==str:  #making the spaces in the grid equal to zero 
            a[j]=0      
            
    for i in range(1,4):  
        m=i
        while a[m-1]==0 and m>0:  #when a number moves from a position it makes that original position zero 
            a[m-1]=a[m]
            a[m]=0 
            m=m-1
            
    for i in range(3):
        if a[i]==a[i+1]:
            a[i]=2*a[i]
            a[i+1]=0
            
    for i in range(1,4):
        m=i
        while a[m-1]==0 and m>0:
            a[m-1]=a[m]
            a[m]=0
            m=m-1    


                     
def push_right(grid): #when the user slides to the right in the game
    for m in range(4):
        a=[grid[m][3],grid[m][2],grid[m][1],grid[m][0]]
        basic(a)
        a.reverse()
        for i in range(4):
            grid[m][i]=a[i]

def push_left(grid): #when the user slides to the left in the game
    for m in range(4):
        a=[grid[m][0],grid[m][1],grid[m][2],grid[m][3]]
        basic(a)
        
        for i in range(4):
            grid[m][i]=a[i] 
            
def push_up(grid): # when the user slides up in the game
    for m in range(4):
        a=[grid[0][m],grid[1][m],grid[2][m],grid[3][m]]
        basic(a)
        for i in range(4):
            grid[i][m]=a[i]
            
def push_down(grid): #when the user slides down in the game
    for m in range(4):
        a=[grid[3][m],grid[2][m],grid[1][m],grid[0][m]]
        basic(a)
        a.reverse()
        for i in range(4):
            grid[i][m]=a[i] 