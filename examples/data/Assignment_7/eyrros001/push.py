"""Push algorithms for 2048 game
Ross Eyre
02/05/2014"""

def push_up (grid):
    """merge grid values upwards"""
    
    #loop through each row
    for col in range(4):
        listCol = []
        for row in range(4):
        #put current row into seperate list
            listCol.append(grid[row][col])
            
        #push up algorithm
        for p in range(3):
            for row in range(4):
                if (row!=3 and listCol[row]==0):
                    #shift all up
                    for i in range(row,3):
                        listCol[i]=listCol[i+1]
                        listCol[i+1]=0
        for row in range(4):            
            if (row!=3 and listCol[row]==listCol[row+1]):
                listCol[row]+=listCol[row+1]
                listCol[row+1]=0
                for i in range(row+1, 3):
                    listCol[i]=listCol[i+1]
                    listCol[i+1]=0           
        
                
            #replace each grid col with updated list
            for row in range(4):
                grid[row][col]=listCol[row]
    

def push_down (grid):
    """merge grid values downwards"""

    #loop through each row
    for col in range(4):
        listCol = []
        for row in range(4):
        #put current row into seperate list
            listCol.append(grid[row][col])
            
        #push down algorithm
        for p in range(3):
            for row in range(3,0,-1):
                if (row!=0 and listCol[row]==0):
                    #shift all down
                    for i in range(row,0,-1):
                        listCol[i]=listCol[i-1]
                        listCol[i-1]=0
        for row in range(3,0,-1):            
            if (row!=0 and listCol[row]==listCol[row-1]):
                listCol[row]+=listCol[row-1]
                listCol[row-1]=0
                #shift zeroes again
                for i in range(row-1, 0,-1):
                    listCol[i]=listCol[i-1]
                    listCol[i-1]=0
                
            #replace each grid col with updated list
            for row in range(4):
                grid[row][col]=listCol[row]
        

def push_left (grid):
    """merge grid values left"""

    #loop through each row
    for row in range(4):
        listRow = []
        for col in range(4):
        #put current row into seperate list
            listRow.append(grid[row][col])
            
        for p in range(3):    
        #push left algorithm
            for col in range(4):
                if (col!=3 and listRow[col]==0):
                    #shift all left:
                    for i in range(col, 3):
                        listRow[i]=listRow[i+1]
                        listRow[i+1]=0
        for col in range(4):            
            if (col!=3 and listRow[col]==listRow[col+1]):
                listRow[col]+=listRow[col+1]
                listRow[col+1]=0
                for i in range(col+1, 3):
                    listRow[i]=listRow[i+1]
                    listRow[i+1]=0                
                        
         #replace each grid row with updated list
            for col in range(4):
                grid[row][col]=listRow[col]


def push_right (grid):
    """merge grid values right"""   

    #loop through each row
    for row in range(4):
        listRow = []
        for col in range(4):
        #put current row into seperate list
            listRow.append(grid[row][col])
            
        #push right algorithm
        for p in range(3):    
            for col in range(3,0,-1):
                if (col!=0 and listRow[col]==0):
                    #shift all right:
                    for i in range(col, 0,-1):
                        listRow[i]=listRow[i-1]
                        listRow[i-1]=0
        for col in range(3,0,-1):            
            if (col!=0 and listRow[col]==listRow[col-1]):
                listRow[col]+=listRow[col-1]
                listRow[col-1]=0
                for i in range(col-1, 0,-1):
                    listRow[i]=listRow[i-1]
                    listRow[i-1]=0
                
        #replace each grid row with updated list
            for col in range(4):
                grid[row][col]=listRow[col] 