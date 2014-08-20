def push_right(grid):

    for k in range(4):
        combinecount=0
        for q in range(3):
            ordlist=[] #resets the ordered list
            for i in range(3,0,-1): #try to combine adjacent numbers if they are equal
                j=i-1
                if grid[k][i]==grid[k][j] and grid[k][j]!=0:
                    grid[k][i]*=2
                    grid[k][j]=0
                    combinecount+=1
                    
            for i in range(4): #create a new list with just the non-zero numbers
                if grid[k][i]!=0:
                    ordlist.append(grid[k][i])

            olength=len(ordlist) 
            for i in range(olength): #put them back into grid in order from the right
                grid[k][3-i]=ordlist[olength-1-i]

            for i in range(4-olength): #set residual numbers to 0
                grid[k][i]=0
            
            if combinecount>0:
                break
    
    return(grid) 

def push_left(grid):
    for k in range(4):
        combinecount=0
        for q in range(3):
            ordlist=[] #resets the ordered list
            for i in range(0,3,1): #try to combine adjacent numbers if they are equal
                j=i+1
                if grid[k][i]==grid[k][j] and grid[k][j]!=0:
                    grid[k][i]*=2
                    grid[k][j]=0
                    combinecount+=1
                    
            for i in range(4): #create a new list with just the non-zero numbers
                if grid[k][i]!=0:
                    ordlist.append(grid[k][i])

            olength=len(ordlist) 
            for i in range(olength): #put them back into grid in order from the right
                grid[k][i]=ordlist[i]

            for i in range(3,olength-1,-1): #set residual numbers to 0
                grid[k][i]=0
            
            if combinecount>0:
                break
            
    return(grid)

def push_up(grid):
    for k in range(4):
        combinecount=0
        for q in range(3):
            ordlist=[] #resets the ordered list
            for i in range(0,3,1): #try to combine adjacent numbers if they are equal
                j=i+1
                if grid[i][k]==grid[j][k] and grid[j][k]!=0:
                    grid[i][k]*=2
                    grid[j][k]=0
                    combinecount+=1
                    
            for i in range(4): #create a new list with just the non-zero numbers
                if grid[i][k]!=0:
                    ordlist.append(grid[i][k])

            olength=len(ordlist) 
            for i in range(olength): #put them back into grid in order from the right
                grid[i][k]=ordlist[i]

            for i in range(3,olength-1,-1): #set residual numbers to 0
                grid[i][k]=0
            
            if combinecount>0:
                break
    
    return(grid)     
    
def push_down(grid):
    for k in range(4):
        combinecount=0
        for q in range(3):
            ordlist=[] #resets the ordered list
            for i in range(3,0,-1): #try to combine adjacent numbers if they are equal
                j=i-1
                if grid[i][k]==grid[j][k] and grid[j][k]!=0:
                    grid[i][k]*=2
                    grid[j][k]=0
                    combinecount+=1
                    
            for i in range(4): #create a new list with just the non-zero numbers
                if grid[i][k]!=0:
                    ordlist.append(grid[i][k])

            olength=len(ordlist) 
            for i in range(olength): #put them back into grid in order from the right
                grid[3-i][k]=ordlist[olength-1-i]

            for i in range(4-olength): #set residual numbers to 0
                grid[i][k]=0
            
            if combinecount>0:
                break
    
    return(grid) 
            
