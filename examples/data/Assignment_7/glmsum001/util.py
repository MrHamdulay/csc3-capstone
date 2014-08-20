#GLMSUM001
#Sumayah Goolam Rassool
# 1 May 2014

hght = 4

#--------------------------------------------Function to create grid-----------------------------------------
def create_grid(grid):
    
    for i in range (hght):
        
        grid.append([0]*4)#-----------------empty grid is created
        
    return grid

#-------------------------------------------------function to print the grid--------------------------------------------   
def print_grid (grid):
    
    wdth = 5 
    
#-------------------------------------------------fills grid

    print("+","-"*20,"+",sep="")
       
    for row in range (hght):
        
        print("|",end="")       
        
        for col in range (hght):
            
            row_x = len(str(grid[row][col]))
            x = int(row_x)     
               
            if "0" in str(grid[row][col]):
                
                print("     ",end="") 
                
            else:
                
                print (grid[row][col],end=(" "*(width-x)))
                
        print("|")     
        
    print("+","-"*20,"+",sep="")    

#------------------------------------------------------------------Check if the game has been lost 

def check_lost (grid):
    
 #---------------------------------------------------checks for any empty spaces within grid and any adjacent  spaces with the same value 
    
    check = True#---------------------creates a boolean value
    
    for col in range (3):       #---------------------goes through each row and column to check if game has been lost
        
        for row in range (4): 
            
            if (str(grid[row][col]) == "0"): 
                
                check = False
                
            elif (grid[row][col] == grid[row][col+1]): 
                
                check = False    
                    
    for row in range (3):
        
        for col in range (4): 
            
            if (str(grid[row][col]) == "0"): 
                
                    check = False
                    
            elif (grid[row][col] == grid[row+1][col]): 
                
                
                    check = False
                    
            
    return check                 
#----------------------------------------------------------------Checks if game has been won by searching through grid for number 32
def check_won (grid):
    
   
    check = True #-----------------------------------------------creating boolean value
    
    for row in range (hght):
        
        for col in range (hght):
            
            x = grid[row][col]  
            
            if (x>=32):   
                
                check = True
                
                if check:
                    
                    return check
                
            else:
                
                check = False
                
    return check                 
 #----------------------------------------------------------------function to copy grid           
def copy_grid (grid): 
    
    
    grid_copy = []   
    
    for i in range(hght):
        
        grid_copy.append(grid[i][:])
        
    return grid_copy            
            

def grid_equal (grid1, grid2):
    
    check = True   
    
    for row in range (hght):
        
        for col in range (hght): 
            
            if not (grid1[row][col]) == (grid2[row][col]):   
                
                return False

    return check                 
    