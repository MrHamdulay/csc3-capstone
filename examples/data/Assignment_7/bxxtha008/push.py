''' program to mirror 2048.py, but only up to 32 - should use 2048.py program and util.py a.k.a Q2
Thabiso Beau
2 May 2014
Assignment 7: push.py'''

#the functions should relatively share the same code as the actions are similar
def push_up (grid):#merge grid values upwards - vertical shift
    #create empty list to append values to it from nested loop
    for x in range(4):
        S =[] #empty list to append values for grid
        T = [] #empty list to append new values in list after the merge
        for y in range(4):
            if grid[x][y]!=0:
                S.append(grid[x][y])
        #introduction of merging process
    for i in range(len(S)):
        if i<len(S):
            if S[i]==S[i+1]:
                T.append(s[i] + s[i+1])
                S.pop(i+1) #remove the a number from the list and assign the value to another number
    grid[i][x] == T[i]
    
    #for z in range(4):
        #grid[x][z] == line(z) #assigning a complete value to the 2-d array
        
def push_down(grid): #doing the same thing as above - vertical shift
    for y in range (3, -1,-1):#descending values as we're shifting it downwards
        S = []          
        T = []
        for z in range(3, -1, -1):
            if grid[y][z]!=0:
                S.append(grid[y][z])
    
    for a in range(len(S)):
        if a>0: #so that list doesn't go out of range
            if S[a] == S[a-1]:
                T.append(S[a] + S[a-1])
                S.pop(a-1)
    grid[y][z] == T[a]
        
def push_left(grid):
#create empty list to append values to it from nested loop
    for x in range(4):
        S =[]
        T = []
        for y in range(4):
            if grid[x][y]!=0:
                S.append(grid[x][y])
                #introduction of merging process
    for i in range(len(S)):
        if i<len(S): #so that list doesn't go out of range
            if S[i]==S[i+1]:
                T.append(s[i] + s[i+1])
                S.pop(i+1)
    grid[i][x] == T[i]    
    

def push_right(grid):
    for y in range (3, -1,-1):
        S = []          
        T = []
        for z in range(3, -1, -1):
            if grid[y][z]!=0:
                S.append(grid[y][z])
       
    for a in range(len(S)):
        if a>0:
            if S[a] == S[a-1]:
                T.append(S[a] + S[a-1])
                S.pop(a-1)
    grid[y][z] == T[a]    