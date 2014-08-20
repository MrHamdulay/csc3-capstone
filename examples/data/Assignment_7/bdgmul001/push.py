# 2048 push module
# mulisa badugela
# 2 May 2014

def push_up (grid):
    
    for row in range(4):
        column=[]
        for col in range(4):
            column.append(grid[col][row])      
        
        for row in range(column.count(0)):
            col=0
            while col<3:
                if column[col]==0:
                    column[col]=column[col+1]
                    column[col+1]-=column[col+1]
                col+=1        
        
        
        i = 0
        while i < 3:
            if column[i] == column[i+1]:
                column[i] *= 2
                column[i+1] *= 0
            i += 1        
    
        for row in range(column.count(0)):
            col=0
            while col<3:
                if column[col]==0:
                    column[col]=column[col+1]
                    column[col+1]-=column[col+1]
                col+=1        

        for i in range(4):
            grid[i][row] = column[i]
          
            
def push_down (grid):
        
    for row in range(4):
        column = []
        for col in range(3,-1,-1):
            column.append(grid[col][row])
        
        for row in range(column.count(0)):
            col=0
            while col<3:
                if column[col]==0:
                    column[col]=column[col+1]
                    column[col+1]-=column[col+1]
                col+=1        
        
        i = 0
        while i < 3:
            if column[i] == column[i+1]:
                column[i] *= 2
                column[i+1] *= 0
            i += 1        
        
        
        for row in range(column.count(0)):
            col=0
            while col<3:
                if column[col]==0:
                    column[col]=column[col+1]
                    column[col+1]-=column[col+1]
                col+=1        
        
        
        x=0
        for i in range(3,-1,-1):
            grid[i][row] = column[x]
            x+=1
    
    
    
def push_left (grid):
    
    for row in range(4):
        rows = []
        for col in range(4):
            rows.append(grid[row][col])
        
        for row in range(rows.count(0)):
            col=0
            while col<3:
                if rows[col]==0:
                    rows[col]=rows[col+1]
                    rows[col+1]-=rows[col+1]
                col+=1         
        
        i = 0
        while i < 3:
            if rows[i] == rows[i+1]:
                rows[i] *= 2
                rows[i+1] *= 0
            i += 1         
        
        for row in range(rows.count(0)):
            col=0
            while col<3:
                if rows[col]==0:
                    rows[col]=rows[col+1]
                    rows[col+1]-=rows[col+1]
                col+=1        
        
        for i in range(4):
            grid[row][i] = rows[i]

def push_right (grid):
     
    for row in range(4):
        rows = []
        for col in range(3,-1,-1):
            rows.append(grid[row][col])
        
        for row in range(rows.count(0)):
            col=0
            while col<3:
                if rows[col]==0:
                    rows[col]=rows[col+1]
                    rows[col+1]-=rows[col+1]
                col+=1        
        
        i = 0
        while i < 3:
            if rows[i] == rows[i+1]:
                rows[i] *= 2
                rows[i+1] *= 0
            i += 1         
        
        for row in range(rows.count(0)):
            col=0
            while col<3:
                if rows[col]==0:
                    rows[col]=rows[col+1]
                    rows[col+1]-=rows[col+1]
                col+=1        
        j=0
        for i in range(3,-1,-1):
            grid[row][i] = rows[j]
            j+=1