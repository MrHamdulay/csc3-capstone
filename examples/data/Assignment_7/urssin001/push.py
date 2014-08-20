'''Complete the code for a 2048 program, using the utility module (util.py) 
and a supplied main program (2048.py).  
The heart of the game is the set of merging functions that merge adjacent equal values and eliminate gaps 
Sinead Urisohn
27 April 2014
'''

def push_up (grid):
  """merge grid values upwards"""
  #change spaces to zeros
  for row in range(4):
    for col in range(4):
      if grid[row][col]==' ':	
        grid[row][col]=0   
  def shiftup(grid):
    #loop through rows and columns
    for row in range(4):
        for col in range(4):
              #shift up by comparing each row to the ones below it
              #check if 0 value
              if grid[0][col]==0:
            
                  #check non-zero value below it
                  if grid[1][col]>0:
                      #shift up
                      grid[0][col]=grid[1][col]
                      grid[1][col]=0
                  elif grid[2][col]>0:
                      grid[0][col]=grid[2][col]
                      grid[2][col]=0
                  elif grid[3][col]>0:
                      grid[0][col]=grid[3][col]
                      grid[3][col]=0            
              elif grid[1][col]==0:
                  if grid[2][col]>0:
                      grid[1][col]=grid[2][col]
                      grid[2][col]=0 
                  elif grid[3][col]>0:
                      grid[2][col]=grid[3][col]
                      grid[3][col]=0          
              
              elif grid[2][col]==0:
                  if grid[3][col]>0:
                      grid[2][col]=grid[3][col]
                      grid[3][col]=0 
  #invoke shiftup
  shiftup(grid)
    
  for row in range(3):#loop 1 less for row to avoid index out of range
      for col in range(4):
          #merge non-zero equal values
          if grid[row+1][col]==grid[row][col] and grid[row][col]>0:
             
            
              #merged value take on double the value
              grid[row][col]=2*grid[row][col]
              #set value merged to zero
              grid[row+1][col]=0
              
            
  #invoke shiftup again to fill gaps left behind after merge
  shiftup(grid) 

def push_down (grid):
    """merge grid values downwards"""
    #change spaces to zeros
    for row in range(4):
       for col in range(4):
         if grid[row][col]==' ':	
           grid[row][col]=0    
    def shiftdown(grid):
        #loop through rows and columns
        for row in range(4):
            for col in range(4):
                #shift down by starting with bottom row and comparing each row above it
                #then moving to the next row and repeat process
                if grid[3][col]==0:
                    if grid[2][col]>0:
                        grid[3][col]=grid[2][col]
                        grid[2][col]=0
                    elif grid[1][col]>0:
                        grid[3][col]=grid[1][col]
                        grid[1][col]=0
                    elif grid[0][col]>0:
                        grid[3][col]=grid[0][col]
                        grid[0][col]=0            
                elif grid[2][col]==0:
                    if grid[1][col]>0:
                        grid[2][col]=grid[1][col]
                        grid[1][col]=0 
                    elif grid[0][col]>0:
                        grid[2][col]=grid[0][col]
                        grid[0][col]=0          
        
                elif grid[1][col]==0:
                    if grid[0][col]>0:
                        grid[1][col]=grid[0][col]
                        grid[0][col]=0   
    shiftdown(grid)
    #merge like values by starting at bottom corner of grid
    for row in range(3,0,-1):#loop 1 less for row to avoid index out of range
        for col in range(3,-1,-1):
            #merge
            if grid[row-1][col]==grid[row][col] and grid[row][col]>0:
               
                grid[row][col]=2*grid[row][col]
                grid[row-1][col]=0
                
    #invoke shift to fill gaps after merge
    shiftdown(grid)     
                

def push_left (grid):
    """merge grid values left"""
    #change spaces to zeros
    for row in range(4):
       for col in range(4):
         if grid[row][col]==' ':	
           grid[row][col]=0    
    def shiftleft(grid):   
        for row in range(4):
            for col in range(4):
              #check if value in grid 0
              if grid[row][col]==0:
                #loop from next col value to end
                for j in range(col+1,4):
                  #if next col value >0
                  if grid[row][j]>0:
                    #send it to col value to left
                    grid[row][col]=grid[row][j]
                    #set value to 0
                    grid[row][j]=0
                    break   
    #invoke first shift    
    shiftleft(grid)
    for row in range(4):
      for col in range(3):#loop 1 less for col to avoid index out of range
        #merge by comparing left-based column values
        if grid[row][col+1]==grid[row][col] and grid[row][col]>0:
          grid[row][col]=2*grid[row][col]
          grid[row][col+1]=0
          break    
    #fill gaps again
    shiftleft(grid)        
def push_right (grid):
    """merge grid values right""" 
    #change spaces to zeros
    for row in range(4):
       for col in range(4):
         if grid[row][col]==' ':	
           grid[row][col]=0    
    def shiftright(grid):
        #loop from bottom of grid because shifting right
        for row in range(3,-1,-1):
            for col in range(3,0,-1):#loop 1 less for col to avoid index out of range
                if grid[row][col]==0:
                    for j in range(col-1,-1,-1):
                        if grid[row][j]>0:
                            grid[row][col]=grid[row][j]
                            grid[row][j]=0
                            break    
    #invoke first shift                      
    shiftright(grid)
    #loop from bottom of grid because merging right
    for row in range(3,-1,-1):
        for col in range(3,0,-1):#loop 1 less for col as need to compare column before it         
            #and do not want to go over index range as only 4x4 grid
            #merge by comparing right-based column values
            if grid[row][col-1]==grid[row][col] and grid[row][col]>0:
    
                grid[row][col]=2*grid[row][col]
                grid[row][col-1]=0
                break
    #fill gaps again
    shiftright(grid)      