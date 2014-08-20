#Keanon Fell
#Assignment 7
#Question 3
#02 May 2014

def push_up (grid):
    #merge grid values upwards
    for vertColumn in range(4): #creates columns
        for horiRow in range(3):
            countValue=1
            while countValue<(4-horiRow) and grid[horiRow][vertColumn]==0: 
                grid[horiRow][vertColumn]=grid[horiRow+countValue][vertColumn]
                grid[horiRow+countValue][vertColumn]=0
                countValue+=1
                
    for vertColumn in range(4): #creates rows
        for horiRow in range(3):
            if grid[horiRow][vertColumn] == grid[horiRow+1][vertColumn]:
                grid[horiRow][vertColumn]=2*grid[horiRow][vertColumn]
                grid[horiRow+1][vertColumn]=0
            
    for vertColumn in range(4):
        for horiRow in range(3):
            countValue=1
            while countValue<(4-horiRow) and grid[horiRow][vertColumn] == 0:
                grid[horiRow][vertColumn]=grid[horiRow+countValue][vertColumn]
                grid[horiRow+countValue][vertColumn]=0
                countValue+=1
            

def push_down (grid):
    #merge grid values downwards
    for vertColumn in range(4):
        for horiRow in range(3,0,-1):
            countValue=1
            while countValue<(horiRow+1) and grid[horiRow][vertColumn]==0:
                grid[horiRow][vertColumn]=grid[horiRow - countValue][vertColumn]
                grid[horiRow - countValue][vertColumn]=0
                countValue+=1
                
    for vertColumn in range(4):
        for horiRow in range(3,0,-1):
            if grid[horiRow][vertColumn]==grid[horiRow-1][vertColumn]:
                grid[horiRow][vertColumn]=2*grid[horiRow][vertColumn]
                grid[horiRow-1][vertColumn]=0
                
    for vertColumn in range(4):
        for horiRow in range(3,0,-1):
            countValue=1
            while countValue<(horiRow+1) and grid[horiRow][vertColumn]==0:
                grid[horiRow][vertColumn]=grid[horiRow-countValue][vertColumn]
                grid[horiRow-countValue][vertColumn]=0
                countValue+=1
                
                
def push_left (grid):
    #merge grid values left
    for horiRow in range(4):
        for vertColumn in range(3):
            countValue=1
            while countValue<(4-vertColumn) and grid[horiRow][vertColumn]==0:
                grid[horiRow][vertColumn]=grid[horiRow][vertColumn+countValue]
                grid[horiRow][vertColumn+countValue]=0
                countValue+=1
                
    for horiRow in range(4):
        for vertColumn in range(3):
            if grid[horiRow][vertColumn]==grid[horiRow][vertColumn+1]:
                grid[horiRow][vertColumn]=2*grid[horiRow][vertColumn]
                grid[horiRow][vertColumn+1]=0
                
    for horiRow in range(4):
        for vertColumn in range(3):
            countValue=1
            while countValue<(4-vertColumn) and grid[horiRow][vertColumn]==0:
                grid[horiRow][vertColumn]=grid[horiRow][vertColumn+countValue]
                grid[horiRow][vertColumn+countValue]=0
                countValue+=1
                

def push_right (grid):
    #merge grid values right 
    for horiRow in range(4):
        for vertColumn in range(3,0,-1):
            countValue=1
            while countValue<(vertColumn+1) and grid[horiRow][vertColumn]==0:
                grid[horiRow][vertColumn]=grid[horiRow][vertColumn-countValue]
                grid[horiRow][vertColumn-countValue]=0
                countValue+=1
                
    for horiRow in range(4):
        for vertColumn in range(3,0,-1):
            if grid[horiRow][vertColumn]==grid[horiRow][vertColumn-1]:
                grid[horiRow][vertColumn]=2*grid[horiRow][vertColumn]
                grid[horiRow][vertColumn-1]=0
                
    for horiRow in range(4):
        for vertColumn in range(3,0,-1):
            countValue=1
            while countValue<(vertColumn+1) and grid[horiRow][vertColumn]==0:
                grid[horiRow][vertColumn]=grid[horiRow][vertColumn-countValue]
                grid[horiRow][vertColumn-countValue]=0
                countValue+=1