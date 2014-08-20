#Emile McLennan
#1 May '14
#A7 Q3

def push_up (grid):
    """merge grid values upwards"""
    merged=[]
    for i in range(5):
        for colNum in range(4):
            for rowNum in range(3):
                        #shift up
                if grid[rowNum][colNum]==0:
                    grid[rowNum][colNum]=grid[rowNum+1][colNum]
                    grid[rowNum+1][colNum]=0
                            
                        #merge identical adjacent values into array into merged 
                elif colNum in merged: 
                    continue
                else:   
                    if grid[rowNum][colNum]==grid[rowNum+1][colNum]:
                        grid[rowNum][colNum]=grid[rowNum][colNum]+grid[rowNum+1][colNum]
                        grid[rowNum+1][colNum]=0
                        merged.append(colNum)

def push_down (grid):
    """merge grid values downwards"""
    merged=[]
    for i in range(5):
        for colNum in range(4):
            for rowNum in range(3, 0, -1):
                            #shift up
                if grid[rowNum][colNum]==0:
                    grid[rowNum][colNum]=grid[rowNum-1][colNum]
                    grid[rowNum-1][colNum]=0
                                
                            #merge identical adjacent values into array into merged
                elif colNum in merged: 
                    continue
                else:   
                    if grid[rowNum][colNum]==grid[rowNum-1][colNum]:
                        grid[rowNum][colNum]=grid[rowNum][colNum]+grid[rowNum-1][colNum]
                        grid[rowNum-1][colNum]=0
                        merged.append(colNum)
                
def push_left (grid):
    """merge grid values left"""
    merged=[]
    for i in range(5):
            for rowNum in range(4):
                for colNum in range(3):
                    #shift left
                    if grid[rowNum][colNum]==0:
                        grid[rowNum][colNum]=grid[rowNum][colNum+1]
                        grid[rowNum][colNum+1]=0
                        
                    #merge identical adjacent values into array into merged
                    elif rowNum in merged: 
                        continue
                    else:
                        if grid[rowNum][colNum]==grid[rowNum][colNum+1]:
                            grid[rowNum][colNum]=grid[rowNum][colNum]+grid[rowNum][colNum+1]
                            grid[rowNum][colNum+1]=0
                            merged.append(rowNum)
                  
def push_right (grid):
    """merge grid values right"""
    merged=[]
    for i in range(5):
            for rowNum in range(4):
                for colNum in range(3,0,-1):
                        #shift right
                    if grid[rowNum][colNum]==0:
                        grid[rowNum][colNum]=grid[rowNum][colNum-1]
                        grid[rowNum][colNum-1]=0
                            
                        #merge identical adjacent values, and put row into a list called merged so that values merge once but not more after the first merge
                    elif rowNum in merged: 
                        continue
                    else:
                        if grid[rowNum][colNum]==grid[rowNum][colNum-1]:
                            grid[rowNum][colNum]=grid[rowNum][colNum]+grid[rowNum][colNum-1]
                            grid[rowNum][colNum-1]=0
                            merged.append(rowNum)
                        
    