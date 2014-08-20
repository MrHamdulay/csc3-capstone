#Konrad Hugo
#2014/05/2
#question 2 Assignment 7

def create_grid(grid):
   
    for i in range(4):           # creates 4 rows through looping               
        grid.append([0,0,0,0])   #creates 4 columns through list of 4 items               
    return grid                                 

def print_grid (grid):
    
    print("+--------------------+")             
    for i in range(4):                 #creates 4x4 grid with 5 width width columns within a box         
        string = "|"                              
        for j in range(4):                      
            value = str (grid[i][j])   #makes a variable representing the (string) value present in the location(grid[i][j])            
            if value == '0':
                value=" "                  #turns all 0's into blank spaces     
            string += value + " " * (5-(len(value)))  
        string += "|"                             
        print(string)                           
    print("+--------------------+")  


def check_lost (grid): #returns boolean:true if no 0's or adjacent equal values
    
    for i in range(4):                          
        for j in range(4):                      
            if grid[i][j]==0:                   
                return False
        for k in range(3):
            if grid[i][k]==grid[i][k+1] or grid[k][i]==grid[k+1][i]:    #check if adjacent values are equal
                return False
    else: return True                           

def check_won (grid): #cheacks for any vallues over or equal to 32 on grid
    
    for i in range(4):                          
        for j in range(4):                      
            if grid[i][j]>=32:                  
                return True                     
    else: return False                          
    
def copy_grid(grid): #Function that copies the grid
    
    for i in range(4):                          
        for j in range(4):                      
            grid[i][j]=str(grid[i][j])          
    for k in range(4):                          
        grid[k]="/".join(grid[k])               
    string="*".join(grid)                       
    grid_copy=string.split("*")                 
    for l in range(4):
        grid_copy[l]=grid_copy[l].split('/')    
    for m in range(4):
        for n in range(4):
            grid_copy[m][n]=eval(grid_copy[m][n])
    for h in range(4):
        grid[h]=grid[h].split('/')              
    for p in range(4):
        for t in range(4):                      
            grid[p][t]=eval(grid[p][t])         
    return grid_copy                            

def grid_equal (grid1, grid2): #Checks if two grids are completely similar and returns false or true
    
    if grid1==grid2:                        
        return True
    else:
        return False