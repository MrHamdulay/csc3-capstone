"""module of merging functions that merge adjacent equal values and eliminate gaps
peter m muriuki"""

#grid = [[4,0,2,0],[0,0,0,0],[0,0,0,0],[0,4,2,0]]

#merge grid values upwards
def push_up (grid):
    n_list=[]
    for c in range(4):
        nlist=[] 
        for r in range (4):
            nlist.append(grid[r][c])       #create individual lists for each column in the grid and add them to nlist
        while 0 in nlist:                  #remove the 0's in the lists
            nlist.remove(0)            
        for i in range (len(nlist)-1):
                #if nlist[i]==0: 
                    #nlist.remove(nlist[i]) 
                #while len(nlist)<4:
                   # nlist.append(0)           
                if nlist[i]==nlist[i+1]:   #check for equal adjacent values and merge them
                    nlist[i]+=nlist[i+1] 
                    nlist[i+1]=0    
        while 0 in nlist:                  #remove the 0's in the list with merged values
            nlist.remove(0) 
        while len(nlist)<4:                #move the 0's to the end in the list
            nlist.append(0)                
        n_list.append(nlist)  
    n_grid=[]  #add all lists to n_grid & replace values in prev grid with values in n_grid
    for c in range (len(n_list)):
        new_list=[]
        for r in range (len(n_list)):    
            new_list.append(n_list[r][c])
        n_grid.append(new_list)
    for r in range(4):
        for c in range(4):
            grid[r][c]=n_grid[r][c]
    return grid

#merge grid values downwards
def push_down (grid):
    n_list=[]
    for c in range(4):
        nlist=[]
        for r in range (4):
            nlist.append(grid[r][c])      #create individual lists for each column in the grid and add them to nlist
        while 0 in nlist:                 #remove the 0's in the lists
            nlist.remove(0)                     
        for i in range (len(nlist)-1):
                #if nlist[i]==0:
                   # nlist.remove(nlist[i]) 
                #while len(nlist)<4:
                  #  nlist.append(0)      
                if nlist[i]==nlist[i+1]:  #check for equal adjacent values and merge them
                    nlist[i]+=nlist[i+1]   
                    nlist[i+1]=0    
        while 0 in nlist:                 #remove the 0's in the list with merged values
            nlist.remove(0) 
        while len(nlist)<4:               #move the 0's to the start of the list
            nlist.insert(0,0)                
        n_list.append(nlist)
    n_grid=[]  #add all lists to n_grid & replace values in prev grid with values in n_grid
    for c in range (len(n_list)):
        new_list=[]
        for r in range (len(n_list)):    
            new_list.append(n_list[r][c])
        n_grid.append(new_list)
    for r in range(4):
        for c in range(4):
            grid[r][c]=n_grid[r][c]     
    return grid

#merge grid values left
def push_left (grid):
    n_list=[]
    for r in range(4):
        nlist=[] 
        for c in range (4):
            nlist.append(grid[r][c])       #create individual lists for each row in the grid and add them to nlist
        while 0 in nlist:                  #remove the 0's in the lists
            nlist.remove(0)
        for i in range (len(nlist)-1):
                #if nlist[i]==0:
                 #   nlist.remove(nlist[i]) 
                #while len(nlist)<4:
                  #  nlist.append(0)       
                if nlist[i]==nlist[i+1]:   #check for equal adjacent values and merge them
                    nlist[i]+=nlist[i+1]    
                    nlist[i+1]=0    
        while 0 in nlist:
            nlist.remove(0)                #remove the 0's in the list with merged values
        while len(nlist)<4:
            nlist.append(0)                #move the 0's to the end in the list       
        n_list.append(nlist) #add all lists to n_list & replace values in given grid with values in n_list
    for r in range(4):
        for c in range(4):
            grid[r][c]=n_list[r][c]
    return grid 

#merge grid values right
def push_right (grid):
    n_list=[]
    for r in range(4):
        nlist=[]
        for c in range (4):
            nlist.append(grid[r][c])       #create individual lists for each row in the grid and add them to nlist
        while 0 in nlist:                  #remove the 0's in the lists
            nlist.remove(0)
        for i in range (len(nlist)-1):
                #if nlist[i]==0:
                   # nlist.remove(nlist[i])  
                #while len(nlist)<4:
                  # nlist.append(0)          
                if nlist[i]==nlist[i+1]:   #check for equal adjacent values and merge them
                    nlist[i]+=nlist[i+1] 
                    nlist[i+1]=0    
        while 0 in nlist:
            nlist.remove(0)                #remove the 0's in the list with merged values
        while len(nlist)<4:
            nlist.insert(0,0)              #move the 0's to the start of the list        
        n_list.append(nlist)   #add all lists to n_list & replace values in given grid with values in n_list
    for r in range(4):
        for c in range(4):
            grid[r][c]=n_list[r][c]
    return grid