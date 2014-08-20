#30 April 2014
#Push functions for 2048
#LYLJON002

def push_up(grid):      #push numbers up
    shift = 0           #intialise loop variable
    while shift < 4:
        shift2 = 0  #intialise loop variable
        
        while shift2 < 3:
            col = shift2+1
            
            while grid [shift2][shift] == 0:    #deletes spaces, moves up
                grid [shift2][shift] = grid [col][shift]
                grid [col][shift] = 0
                col = col + 1
                if col == 4:
                    break 
                
            shift2 = shift2 + 1     #change while loop vairable
            
        shift2 = 0                  #intialise loop variable
        while shift2 < 3:          #adds numbers
            if grid [shift2][shift] == grid [shift2+1][shift]:
                grid [shift2][shift] = grid [shift2][shift] + grid [shift2][shift]
                grid [shift2+1][shift] = 0
            
            col=shift2+1
            while grid [shift2][shift] == 0:    #deletes spaces
                grid [shift2][shift] = grid [col][shift]
                grid [col][shift] = 0
                col = col + 1
                if col == 4:
                    break
            shift2 = shift2 + 1  #change while loop vairable
        shift = shift + 1        #change while loop vairable

def push_down(grid):      #move numebrs down
    shift = 0               #intialise loop variable
   
    while shift < 4:
        shift2 = 3      #intialise loop variable
       
        while shift2 > -1:
            col=shift2
           
            while grid [shift2][shift] == 0:    #deletes spaces, moves downwards
                grid [shift2][shift] = grid [col][shift]
                grid [col][shift]=0
                col = col - 1
                if col == -1:
                    break  
            shift2 = shift2 - 1  #change while loop vairable
       
        shift2 = 3      #intialise loop variable
       
        while shift2 > -1:          #adds numbers, moves them down
            if grid [shift2][shift] == grid [shift2-1][shift]:
                grid [shift2][shift] = grid [shift2][shift] + grid[shift2][shift]
                grid [shift2-1][shift] = 0
            
            col = shift2
           
            while grid [shift2][shift] == 0:    #deletes spaces
                grid [shift2][shift] = grid [col][shift]
                grid [col][shift] = 0
                col = col - 1
                if col == -1:
                    break
            shift2 = shift2 - 1  #change while loop vairable
        shift = shift + 1        #change while loop vairable

def push_left(grid):            #moves numbers left
    shift = 0                               #intialise loop variable
    
    while shift < 4:
        
        shift2 = 0
        while shift2 < 3:
            row = shift2 + 1
          
            while grid [shift][shift2] == 0:    #deletes spaces, moves left
                grid [shift][shift2] = grid [shift][row]
                grid [shift][row] = 0
                row = row + 1
                if row == 4:
                    break    
    
            shift2 = shift2 + 1     #change while loop vairable
        
        shift2 = 0              #intialise loop variable
       
        while shift2 < 3:          #adds numbers, moving left
           
            if grid [shift][shift2] == grid [shift][shift2+1]:
                grid [shift][shift2] = grid [shift][shift2] + grid [shift][shift2]
                grid [shift][shift2+1] = 0
            
            row = shift2+1
           
            while grid [shift][shift2] == 0:    #deletes spaces
                grid [shift][shift2] = grid [shift][row]
                grid [shift][row] = 0
                row = row + 1
                
                if row == 4:
                    break
            shift2 = shift2 + 1  #change while loop vairable
        shift = shift + 1        #change while loop vairable
                
def push_right(grid):      #moves numbers right
    shift = 0               #intialise loop variable
 
    while shift < 4:
        shift2 = 3
       
        while shift2 > -1:
            row = shift2
           
            while grid [shift][shift2] == 0:    #deletes spaces, moves right
                grid [shift][shift2] = grid [shift][row]
                grid [shift][row] = 0
                row = row - 1
                
                if row ==-1:
                    break 
                
            shift2 = shift2 - 1  #change while loop vairable
        shift2 = 3                      #intialise loop variable
       
        while shift2 > - 1:          #adds numbers, moving them right
            if grid [shift][shift2] == grid [shift][shift2-1]:
                grid [shift][shift2] = grid [shift][shift2] + grid [shift][shift2]
                grid [shift][shift2-1] = 0
            
            row = shift2
           
            while grid [shift][shift2] == 0:    #deletes spaces
                grid [shift][shift2] = grid [shift][row]
                grid [shift][row] = 0
                row = row - 1
                if row == -1:
                    break
                
            shift2 = shift2 - 1  #change while loop variable
        shift = shift + 1       #change while loop variable