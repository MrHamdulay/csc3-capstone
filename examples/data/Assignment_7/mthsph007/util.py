""" Sphiwe Muthembi
    MTHSPH007
    Assignment 7 - Question 2"""

#create functions:
def create_grid(grid):
    
    #Agrid = [0,0,0,0]
    
    #grid = Agrid[0]*4
    for i in range(4):
        grid.append([0]*4)
    
    return grid
#grid = []
#print(create_grid2(grid))

def create_grid2(grid):
    Agrid = [ '','','','']
    #grids = []
    for i in range (4):
        grid.append(Agrid)
    
    return grid 


#grid =[]               
#print(create_grid(grid))     # test line
def print_grid (grid):
    
    
    print ('+'+'-'*20+'+')
    for i in range (len (grid)):
        p = grid[i]
        out = ''
        for j in range(len(p)):
            if p[j] == 0:
                out += ' '* 5
            else:
                
                out += str(p[j]) +' '*(5- len(str(p[j])))
          #  print(p[j])
        
       # print(out)
        print ('|'+out+'|' )
            
    print ('+'+'-'*20+'+')
    
   

#print_grid(create_grid(0))     #test line
#===================================
def check_lost(grid):
    for i in range( len(grid)):
                            
        for k in range( len(grid[i])):    
    
            #use while loop to check through grid for equal adjacent values and empty values.              and grid[i][k] != grid[i+1][k]  or grid[i-1][k]
        
            count = 1
            while count < 4:
                                
                if grid[i][k] == 32:
                    return True                    
                elif grid[i][k] != 0  and grid[i][k] != grid[i][k + count] and grid[i][k] != grid[i][k -count]  and grid[i][k] != grid[i + count][k] and grid[i][k] != grid[i-count][k]:
                    return True
                 
                count+=1
            else:
                return False                  
                           
                
#print(check_lost(create_grid(3)) )         test line         
#========================================================
def check_won (grid):
    count =0
    while count < len(grid):
        for i in range (len(grid)):
            for j in range(len(grid[i])):
                
            
                
                if grid[i][j] >= 32:
                    return True
        count +=1
    else:
        return False
        
#=========================================================            
import copy
def copy_grid(grid):
    
    grid_copied = []
    grid_copied = copy.deepcopy(grid)
  
    return grid_copied

#h = [0,3,2,0]
#print (copy_grid(h))    
#========================================================

def grid_equal (grid1,grid2):
   # count = 0
    match_add = 0
    #while count < len(grid1):
        
    for i in range (len(grid1)):
        for j in range( len(grid1)):
            
            if grid1[i][j] == grid2[i][j]:
                match_add+=1
                    #return True
                    
       # count+=1  
    if match_add >= 16:
        return True
    else:
        return False


