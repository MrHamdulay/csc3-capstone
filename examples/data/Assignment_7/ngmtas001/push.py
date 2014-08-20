#Question3
#Tase Ngambi
#28 April 2014

# grid utility routines
import util

#grid = []
#util.create_grid(grid)
#grid = [[0,0,0,1],[0,2,0,0],[2,2,3,0],[0,1,0,1]]
#util.print_grid(grid)

def push_up(grid):

    #setting blanks to zero
    for y in range(4):
        for x in range(4):
            if grid[y][x] == " ":
                grid[y][x] =0
    #checking variations of cases            
    case = 0
    for x in range(4):
        if grid[3][x] != 0 and grid[2][x] != 0:
            case =1
            break
        elif grid[2][x] != 0 and grid[1][x] != 0:
            case =1   
            break
        elif grid[1][x] != 0 and grid[0][x] != 0:
            case =1  
            break
        elif grid[3][x] != 0 and grid[1][x] != 0:
            case =2
            break
        elif grid[2][x] != 0 and grid[0][x] != 0:
            case =2 
            break
        elif grid[3][x] != 0 and grid[0][x] != 0:
            case = 3
            break
        else:
            case =0
            
        
    #shifting of elements upwards 
    for x in range(4):
        
        if case ==0:
            if grid[3][x] != 0:
                grid[3][x], grid[0][x] = grid[0][x],grid[3][x]
            elif grid[2][x] != 0:
                grid[2][x], grid[0][x] = grid[0][x],grid[2][x]
            elif grid[1][x] != 0:
                grid[1][x], grid[0][x] = grid[0][x],grid[1][x]    
                
                
       
        if case ==1:
            if grid[3][x] != 0 and grid[2][x] != 0:
                SumAdj = int(grid[3][x]) + int(grid[2][x])
                
                if grid[0][x] == 0:
                    grid[2][x] =0
                    grid[3][x], grid[0][x] = 0, SumAdj
                    
                else:
                    grid[3][x], grid[2][x] = 0, SumAdj
                
            elif grid[2][x] != 0 and grid[1][x] != 0:
                SumAdj = int(grid[2][x]) + int(grid[1][x])
                if grid[0][x] == 0:
                    grid[1][x] =0
                    grid[2][x], grid[0][x] = 0, SumAdj
                else:   
                    grid[2][x], grid[1][x] = 0, SumAdj
                
            elif grid[1][x] != 0 and grid[0][x] != 0:
                SumAdj = int(grid[1][x]) + int(grid[0][x])
                grid[1][x], grid[0][x] = 0, SumAdj            
            
            
            elif grid[3][x] != 0 and grid[2][x] == 0 and grid[1][x] == 0:
                grid[3][x], grid[0][x] = grid[0][x], grid[3][x]
            
            
            elif grid[2][x] != 0 and grid[3][x] == 0 and grid[1][x] == 0:
                grid[2][x], grid[0][x] = grid[0][x], grid[2][x]            


            elif grid[1][x] != 0 and grid[3][x] == 0 and grid[2][x] == 0:
                grid[1][x], grid[0][x] = grid[0][x], grid[1][x]            
         
         
        if case ==2:
            if grid[3][x] != 0 and grid[1][x] != 0:
                SumAdj = int(grid[3][x]) + int(grid[1][x])
                if grid[0][x] == 0:
                    grid[1][x] =0
                    grid[3][x], grid[0][x] = 0, SumAdj
                else:
                    grid[3][x], grid[1][x] = 0, SumAdj 
                
            elif grid[2][x] != 0 and grid[0][x] != 0:
                SumAdj = int(grid[2][x]) + int(grid[0][x])
                grid[2][x], grid[0][x] = 0, SumAdj 
                    
    
            elif grid[3][x] != 0 and grid[2][x] == 0 and grid[1][x] == 0:
                grid[3][x], grid[0][x] = grid[0][x], grid[3][x]
            
            
            elif grid[2][x] != 0 and grid[3][x] == 0 and grid[1][x] == 0:
                grid[2][x], grid[0][x] = grid[0][x], grid[2][x]            


            elif grid[1][x] != 0 and grid[3][x] == 0 and grid[2][x] == 0:
                grid[1][x], grid[0][x] = grid[0][x], grid[1][x]                 
                
            
        if case ==3:
            if grid[3][x] != 0 and grid[0][x] != 0:
                SumAdj = int(grid[3][x]) + int(grid[0][x])
                grid[3][x], grid[0][x] = 0, SumAdj
                    
            elif grid[3][x] != 0 and grid[0][x] == 0:
                grid[3][x], grid[0][x] = grid[0][x], grid[3][x]
            
            elif grid[2][x] != 0 and grid[0][x] == 0:
                grid[2][x], grid[0][x] = grid[0][x], grid[2][x]  
                
            elif grid[1][x] != 0 and grid[0][x] == 0:
                grid[1][x], grid[0][x] = grid[0][x], grid[1][x]                  


def push_down(grid):

    #setting blanks to zero
    for y in range(4):
        for x in range(4):
            if grid[y][x] == " ":
                grid[y][x] =0
    #checking variations of cases            
    case = 0
    for x in range(4):
        if grid[3][x] != 0 and grid[2][x] != 0:
            case =1
            break
        elif grid[2][x] != 0 and grid[1][x] != 0:
            case =1   
            break
        elif grid[1][x] != 0 and grid[0][x] != 0:
            case =1  
            break
        elif grid[3][x] != 0 and grid[1][x] != 0:
            case =2
            break
        elif grid[2][x] != 0 and grid[0][x] != 0:
            case =2 
            break
        elif grid[3][x] != 0 and grid[0][x] != 0:
            case = 3
            break
        else:
            case =0
            
            
    
    #shifting of elements upwards 
    for x in range(4):
        
        if case ==0:
            if grid[0][x] != 0:
                grid[0][x], grid[3][x] = grid[3][x],grid[0][x]
            elif grid[2][x] != 0:
                grid[2][x], grid[3][x] = grid[3][x],grid[2][x]
            elif grid[1][x] != 0:
                grid[1][x], grid[3][x] = grid[3][x],grid[1][x]        
        
        
        if case ==1:
            
            
            if grid[1][x] != 0 and grid[0][x] != 0:
                    SumAdj = int(grid[1][x]) + int(grid[0][x])
                    if grid[3][x] == 0:
                        grid[1][x] =0
                        grid[0][x], grid[3][x] = 0, SumAdj
                    else:
                        grid[0][x], grid[1][x] = 0, SumAdj
                    
            elif grid[2][x] != 0 and grid[1][x] != 0:
                    SumAdj = int(grid[2][x]) + int(grid[1][x])
                    if grid[3][x] ==0:
                        grid[2][x] =0
                        grid[1][x], grid[3][x] = 0, SumAdj  
                    else:
                        grid[1][x], grid[2][x] = 0, SumAdj  
                            
                            
            elif grid[3][x] != 0 and grid[2][x] != 0:
                SumAdj = int(grid[3][x]) + int(grid[2][x])
                grid[2][x], grid[3][x] = 0, SumAdj
                
              
                                
            elif grid[2][x] != 0 and grid[3][x] == 0:
                grid[3][x], grid[2][x] = grid[2][x], grid[3][x]
            
            elif grid[1][x] != 0 and grid[2][x] == 0:
                grid[3][x], grid[1][x] = grid[1][x], grid[3][x] 
                
            elif grid[0][x] != 0 and grid[1][x] == 0:
                grid[3][x], grid[0][x] = grid[0][x], grid[3][x]            
         
         
        if case ==2:
        
            if grid[2][x] != 0 and grid[0][x] != 0:
                SumAdj = int(grid[2][x]) + int(grid[0][x])
                if grid[3][x] == 0:
                    grid[2][x] =0
                    grid[0][x], grid[3][x] = 0, SumAdj            
                else:
                    grid[0][x], grid[2][x] = 0, SumAdj 
           
            elif grid[3][x] != 0 and grid[1][x] != 0:
                SumAdj = int(grid[3][x]) + int(grid[1][x])
                grid[1][x], grid[3][x] = 0, SumAdj
                
            
            elif grid[2][x] != 0 and grid[3][x] == 0:
                grid[3][x], grid[2][x] = grid[2][x], grid[3][x]
            
            elif grid[1][x] != 0 and grid[2][x] == 0:
                grid[3][x], grid[1][x] = grid[1][x], grid[3][x] 
                
            elif grid[0][x] != 0 and grid[1][x] == 0:
                grid[3][x], grid[0][x] = grid[0][x], grid[3][x]              
                
            
        if case ==3:
            if grid[3][x] != 0 and grid[0][x] != 0:
                SumAdj = int(grid[3][x]) + int(grid[0][x])
                grid[0][x], grid[3][x] = 0, SumAdj
                    
            elif grid[0][x] != 0 and grid[3][x] == 0:
                grid[3][x], grid[0][x] = grid[0][x], grid[3][x]
            
            elif grid[0][x] != 0 and grid[2][x] == 0:
                grid[2][x], grid[0][x] = grid[0][x], grid[2][x]  
                
            elif grid[0][x] != 0 and grid[1][x] == 0:
                grid[1][x], grid[0][x] = grid[0][x], grid[1][x]                  


def push_left(grid):

    #setting blanks to zero
    for y in range(4):
        for x in range(4):
            if grid[y][x] == " ":
                grid[y][x] =0
    #checking variations of cases            
    case = 0
    for x in range(4):
        if grid[x][3] != 0 and grid[x][2] != 0:
            case =1
            break
        elif grid[x][2] != 0 and grid[x][1] != 0:
            case =1   
            break
        elif grid[x][1] != 0 and grid[x][0] != 0:
            case =1  
            break
        elif grid[x][3] != 0 and grid[x][1] != 0:
            case =2
            break
        elif grid[x][2] != 0 and grid[x][0] != 0:
            case =2 
            break
        elif grid[x][3] != 0 and grid[x][0] != 0:
            case = 3
            break
        else:
            case =0
            
            
    
    #shifting of elements upwards 
    for x in range(4):
        
        if case ==0:
            if grid[x][3] != 0:
                grid[x][3], grid[x][0] = grid[x][0],grid[x][3]
            elif grid[x][2] != 0:
                grid[x][2], grid[x][0] = grid[x][0],grid[x][2]
            elif grid[x][1] != 0:
                grid[x][1], grid[x][0] = grid[x][0],grid[x][1]      
    
      
        if case ==1:
                    
        
            if grid[x][3] != 0 and grid[x][2] != 0:
                SumAdj = int(grid[x][3]) + int(grid[x][2])
                if grid[x][0] == 0:
                    grid[x][2] = 0
                    grid[x][3], grid[x][0] = 0, SumAdj
                else:
                    grid[x][2], grid[x][0] = 0, SumAdj
            
            elif grid[x][2] != 0 and grid[x][1] != 0:
                SumAdj = int(grid[x][2]) + int(grid[x][1])
                if grid[x][0] == 0:
                    grid[x][1] = 0
                    grid[x][2], grid[x][0] = 0, SumAdj             
                else:
                    grid[x][2], grid[x][1] = 0, SumAdj 
                    
            
            elif grid[x][1] != 0 and grid[x][0] != 0:
                SumAdj = int(grid[x][1]) + int(grid[x][0])
                grid[x][1], grid[x][0] = 0, SumAdj  
                
                           
            elif grid[x][3] != 0 and grid[x][2] == 0:
                grid[x][3], grid[x][0] = grid[x][0], grid[x][3]
            
            elif grid[x][2] != 0 and grid[x][1] == 0:
                grid[x][2], grid[x][0] = grid[x][0], grid[x][2] 
                
            elif grid[x][1] != 0 and grid[x][0] == 0:
                grid[x][1], grid[x][0] = grid[x][0], grid[x][1]            
         
         
        
     

        
        
        
        
        
        elif case ==3:
            if grid[x][3] != 0 and grid[x][0] != 0:
                SumAdj = int(grid[x][3]) + int(grid[x][0])
                grid[x][3], grid[x][0] = 0, SumAdj
                    
            elif grid[x][3] != 0 and grid[x][0] == 0:
                grid[x][3], grid[x][0] = grid[x][0], grid[x][3]
            
            elif grid[x][2] != 0 and grid[x][0] == 0:
                grid[x][2], grid[x][0] = grid[x][0], grid[x][2]  
                
            elif grid[x][1] != 0 and grid[x][0] == 0:
                grid[x][1], grid[x][0] = grid[x][0], grid[x][1]  
                
        elif case ==2:
                    
            if grid[x][2] != 0 and grid[x][0] != 0:
                SumAdj = int(grid[x][2]) + int(grid[x][0])
                grid[x][2], grid[x][0] = 0, SumAdj   
                
                
            elif grid[x][3] != 0 and grid[x][1] != 0:
                SumAdj = int(grid[x][3]) + int(grid[x][1])
                if grid[x][0] ==0:
                    grid[x][1] =0
                    grid[x][3], grid[x][0] = 0, SumAdj
                else:
                    grid[x][3], grid[x][1] = 0, SumAdj 
              
                    
            elif grid[x][3] != 0 and grid[x][0] == 0:
                grid[x][3], grid[x][0] = grid[x][0], grid[x][3]
            
            elif grid[x][2] != 0 and grid[x][0] == 0:
                grid[x][2], grid[x][0] = grid[x][0], grid[x][2]  
                
            elif grid[x][1] != 0 and grid[x][0] == 0:
                grid[x][1], grid[x][0] = grid[x][0], grid[x][1]                 
                
                
                                        
def push_right(grid):

    #setting blanks to zero
    for y in range(4):
        for x in range(4):
            if grid[y][x] == " ":
                grid[y][x] =0
    #checking variations of cases            
    case = 0
    for x in range(4):
        if grid[x][3] != 0 and grid[x][2] != 0:
            case =1
            break
        elif grid[x][2] != 0 and grid[x][1] != 0:
            case =1   
            break
        elif grid[x][1] != 0 and grid[x][0] != 0:
            case =1  
            break
        elif grid[x][3] != 0 and grid[x][1] != 0:
            case =2
            break
        elif grid[x][2] != 0 and grid[x][0] != 0:
            case =2 
            break
        elif grid[x][3] != 0 and grid[x][0] != 0:
            case = 3
            break
        else: 
            case =0
            
            
    
    #shifting of elements upwards 
    for x in range(4):
        
        
        if case ==0:
            if grid[x][0] != 0:
                grid[x][3], grid[x][0] = grid[x][0],grid[x][3]
            elif grid[x][2] != 0:
                grid[x][2], grid[x][3] = grid[x][3],grid[x][2]
            elif grid[x][1] != 0:
                grid[x][1], grid[x][3] = grid[x][3],grid[x][1]       
    
    
        
        if case ==1:
                    
        
            if grid[x][2] != 0 and grid[x][3] != 0:
                SumAdj = int(grid[x][3]) + int(grid[x][2])
                grid[x][2], grid[x][3] = 0, SumAdj
            
            elif grid[x][1] != 0 and grid[x][2] != 0:
                SumAdj = int(grid[x][2]) + int(grid[x][1])
                if grid[x][3] == 0:
                    grid[x][2] = 0
                    grid[x][1], grid[x][3] = 0, SumAdj             
            
                else:
                    grid[x][1], grid[x][2] = 0, SumAdj 
                        
            elif grid[x][0] != 0 and grid[x][1] != 0:
                SumAdj = int(grid[x][1]) + int(grid[x][0])
                if grid[x][3] ==0:
                    grid[x][1] =0
                    grid[x][0], grid[x][3] = 0, SumAdj  
                else:
                    grid[x][0], grid[x][1] = 0, SumAdj 
                           
    
            elif grid[x][2] != 0 and grid[x][3] == 0:
                grid[x][3], grid[x][2] = grid[x][2], grid[x][3]
            
            elif grid[x][1] != 0 and grid[x][2] == 0:
                grid[x][3], grid[x][1] = grid[x][1], grid[x][3] 
                
            elif grid[x][0] != 0 and grid[x][1] == 0:
                grid[x][3], grid[x][0] = grid[x][0], grid[x][3]            
         
         
        
     

        
        
        
        
        
        elif case ==3:
            if grid[x][3] != 0 and grid[x][0] != 0:
                SumAdj = int(grid[x][3]) + int(grid[x][0])
                grid[x][0], grid[x][3] = 0, SumAdj
            
            elif grid[x][2] != 0 and grid[x][3] == 0:
                grid[x][3], grid[x][2] = grid[x][2], grid[x][3]
            
            elif grid[x][1] != 0 and grid[x][2] == 0:
                grid[x][3], grid[x][1] = grid[x][1], grid[x][3] 
                
            elif grid[x][0] != 0 and grid[x][1] == 0:
                grid[x][3], grid[x][0] = grid[x][0], grid[x][3]  
                
        elif case ==2:
                    
            if grid[x][2] != 0 and grid[x][0] != 0:
                SumAdj = int(grid[x][2]) + int(grid[x][0])
                if grid[x][3] ==0:
                    grid[x][2] = 0
                    grid[x][0], grid[x][3] = 0, SumAdj   
                
                else:
                    grid[x][0], grid[x][2] = 0, SumAdj
                    
            elif grid[x][3] != 0 and grid[x][1] != 0:
                SumAdj = int(grid[x][3]) + int(grid[x][1])
                grid[x][1], grid[x][3] = 0, SumAdj
                
              
            elif grid[x][2] != 0 and grid[x][3] == 0:
                grid[x][3], grid[x][2] = grid[x][2], grid[x][3]
            
            elif grid[x][1] != 0 and grid[x][2] == 0:
                grid[x][3], grid[x][1] = grid[x][1], grid[x][3] 
                
            elif grid[x][0] != 0 and grid[x][1] == 0:
                grid[x][3], grid[x][0] = grid[x][0], grid[x][3] 
                
                                                
        
        
                
                
        
     
     
    
    
#push_left(grid)
#util.print_grid(grid)  
    
    
   
      
    