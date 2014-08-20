#Kovlin Perumal
#PRMKOV001
#30/04/2014
#Question 2 - 2048 Pushes

def push_up (grid):
    alreadymulti = []
    for i in range (4):
        for j in range (4):
            if grid[i][j]!= 0 and i != 0:
                count = i - 1
                while (grid[count][j] == 0) and (count > 0) :
                    count-=1                
                if grid[count][j] == 0 :
                    grid[count][j] = grid[i][j]
                    grid[i][j] = 0
                elif grid[count][j] == grid [i][j] and ((count, j) not in alreadymulti):
                    grid[count][j]*=2
                    grid[i][j] = 0
                    alreadymulti.append((count, j))
                else :                    
                    grid[count + 1][j] = grid[i][j]
                    if (count + 1) != i:
                        grid[i][j] = 0
        
def push_down (grid):
    """merge grid values downwards"""
    alreadymulti = []
    for i in range (3,-1,-1):
            for j in range (4):
                if grid[i][j]!= 0 and i != 3:
                    count = i + 1
                    while (grid[count][j] == 0) and (count < 3) :
                        count+=1                    
                    if grid[count][j] == 0 :
                        grid[count][j] = grid[i][j]
                        grid[i][j] = 0
                    elif grid[count][j] == grid [i][j] and ((count, j) not in alreadymulti):
                        grid[count][j]*=2
                        grid[i][j] = 0
                        alreadymulti.append((count, j))
                    else:
                        grid[count - 1][j] = grid[i][j]
                        if (count - 1) != i:
                            grid[i][j] = 0    

def push_left (grid):
    """merge grid values left"""
    alreadymulti = []
    for i in range (4):
            for j in range (4):
                if grid[i][j]!= 0 and j != 0:
                    count = j - 1
                    while (grid[i][count] == 0) and (count > 0) :
                        count-=1                
                    if grid[i][count] == 0 :
                        grid[i][count] = grid[i][j]
                        grid[i][j] = 0
                    elif grid[i][count] == grid [i][j] and ((count, i) not in alreadymulti):
                        grid[i][count]*=2
                        grid[i][j] = 0
                        alreadymulti.append((count, i))
                    else :                    
                        grid[i][count + 1] = grid[i][j]
                        if (count + 1) != j:
                            grid[i][j] = 0    

def push_right (grid):
    """merge grid values right"""  
    alreadymulti = []
    for i in range (4):
                for j in range (3, -1, -1):
                    if grid[i][j]!= 0 and j != 3:
                        count = j + 1
                        while (grid[i][count] == 0) and (count < 3) :
                            count+=1                    
                        if grid[i][count] == 0 :
                            grid[i][count] = grid[i][j]
                            grid[i][j] = 0
                        elif grid[i][count] == grid [i][j] and ((i, count) not in alreadymulti):
                            grid[i][count]*=2
                            grid[i][j] = 0
                            alreadymulti.append((i, count))
                        else:
                            grid[i][count - 1] = grid[i][j]
                            if (count - 1) != j:
                                grid[i][j] = 0    
    
testGrid = [[8,4,4,0],[4,0,0,0],[2,0,2,0],[0,0,2,0]]

"""for i in testGrid :
    print(i)
    
push_right(testGrid)
print()

for i in testGrid :
    print(i)"""

