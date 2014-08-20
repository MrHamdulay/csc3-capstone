"""Kureshlen Moodley
MDLKUR001
3 May 20114"""

#make a grid
def create_grid(x):
    for i in range(4):
        x.append ([0]*4)
    
    return x
#display grid
    
def print_grid(x):
    print("+--------------------+")
    
    for i in range(4):
        print("|", end="")
        for r in range(4):
            if str(grid[i][r])=="0":
              
                print(" "*5,end="")
            else:
                print("{0:<5}".format(str(grid[i][r])), end="")
            
        print("|")
    print("+--------------------+")
    
# check lost grid    
    
def check_lost(x):
    for i in range(4):
        for r in range(4):
           
           
            if str(x[i][r])==0:
                return False
           
           
            elif r+1<4 and str(x[i][r])==str(x[i][r+1]):
                return False
            
            elif i+1<4 and str(x[i][r])==str(x[i+1][r]):
                return False
            
    return True
#won
def check_won(x):
    for i in range(4):
        
        for r in range(4):
            if str(x[i][j])>="32":
               
                return True
            else:
               
                return False
#duplicate grid            

def copy_grid(x):
    grid1=[]
    
    
    for i in range(4):
        listw=[]
       
       
        for r in range(4):
            a.append(x[i][r])
        grid1.append(listw)
    return grid1
    
def kuresh(grid1,grid2):
    
    
    for i in range(4):
        
        
        for r in range(4):
            if str(grid1[i][r])==str(grid2[i][r]):
                return True
           
           
            else:
                return False      
        