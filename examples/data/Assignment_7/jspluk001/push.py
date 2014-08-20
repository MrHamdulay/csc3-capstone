'''Luke Joseph
2014-04-28
question 3 of assignment 7'''

def push_left(grid):
    
    # pushing values leftwards for every possible scenario. 
    for i in range(4): 
        if grid[i][0]==0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]==0:
            pass
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]!=0:
            pass
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]==0:
            pass
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]==0:
            pass
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]==0:
            pass
        elif grid[i][0]==0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]!=0:
            grid[i][0]=grid[i][3] 
            grid[i][3]=0
        elif grid[i][0]==0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]!=0:
            grid[i][0]=grid[i][2] 
            grid[i][1]=grid[i][3] 
            grid[i][2]=0 
            grid[i][3]=0
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]!=0:
            grid[i][0]=grid[i][1] 
            grid[i][1]=grid[i][2] 
            grid[i][2]=grid[i][3] 
            grid[i][3]=0
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]==0:
            grid[i][1]=grid[i][2] 
            grid[i][2]=0 
            grid[i][3]=0
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]!=0:
            grid[i][0]=grid[i][1] 
            grid[i][1]=grid[i][3] 
            grid[i][2]=0 
            grid[i][3]=0
        elif grid[i][0]==0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]==0:
            grid[i][0]=grid[i][2] 
            grid[i][1]=0 
            grid[i][2]=0 
            grid[i][3]=0
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]==0:
            grid[i][0]=grid[i][1] 
            grid[i][1]=0 
            grid[i][2]=0 
            grid[i][3]=0
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]!=0:
            grid[i][1]=grid[i][3] 
            grid[i][2]=0 
            grid[i][3]=0
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]==0:
            grid[i][0]=grid[i][1] 
            grid[i][1]=grid[i][2] 
            grid[i][2]=0 
            grid[i][3]=0
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]!=0:
            grid[i][1]=grid[i][2] 
            grid[i][2]=grid[i][3] 
            grid[i][3]=0
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]!=0:
            grid[i][2]=grid[i][3] 
            grid[i][3]=0
            
            # Adding adjacent numbers.
        if grid[i][0]==grid[i][1]:
            grid[i][0]=grid[i][0]+grid[i][1]
            grid[i][1]=grid[i][2]
            grid[i][2]=grid[i][3]
            grid[i][3]=0
        if grid[i][1]==grid[i][2]:
            grid[i][1]=grid[i][1]+grid[i][2]
            grid[i][2]=grid[i][3]
            grid[i][3]=0
        if grid[i][2]==grid[i][3]:
            grid[i][2]=grid[i][2]+grid[i][3]
            grid[i][3]=0
            
def push_right(grid):
    
    # Pushing values rightwards for every possible scenario.
    for i in range(4): 
        if grid[i][0]==0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]==0:
            pass
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]!=0:
            pass
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]==0:
            grid[i][3]=grid[i][0]
            grid[i][0]=0
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]==0:
            grid[i][3]=grid[i][1]
            grid[i][2]=grid[i][0]
            grid[i][0]=0
            grid[i][1]=0
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]==0:
            grid[i][3]=grid[i][2]
            grid[i][2]=grid[i][1]
            grid[i][1]=grid[i][0]
            grid[i][0]=0
        elif grid[i][0]==0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]!=0:
            pass
        elif grid[i][0]==0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]!=0:
            pass
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]!=0:
            pass
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]==0:
            grid[i][3]=grid[i][2]
            grid[i][2]=grid[i][0] 
            grid[i][0]=0
            grid[i][1]=0 
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]!=0:
            grid[i][2]=grid[i][1]
            grid[i][0]=0 
            grid[i][1]=0 
        elif grid[i][0]==0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]==0:
            grid[i][3]=grid[i][2]
            grid[i][0]=0 
            grid[i][1]=0 
            grid[i][2]=0 
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]==0:
            grid[i][3]=grid[i][1]
            grid[i][0]=0 
            grid[i][1]=0 
            grid[i][2]=0 
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]==0 and grid[i][3]!=0:
            grid[i][2]=grid[i][0]
            grid[i][0]=0
            grid[i][1]=0
        elif grid[i][0]==0 and grid[i][1]!=0 and grid[i][2]!=0 and grid[i][3]==0:
            grid[i][3]=grid[i][2]
            grid[i][2]=grid[i][1] 
            grid[i][0]=0 
            grid[i][1]=0 
        elif grid[i][0]!=0 and grid[i][1]==0 and grid[i][2]!=0 and grid[i][3]!=0:
            grid[i][1]=grid[i][0]
            grid[i][0]=0
        elif grid[i][0]!=0 and grid[i][1]!=0 and grid[i][2]==0 and grid[i][3]!=0:
            grid[i][2]=grid[i][1]
            grid[i][1]=grid[i][0]
            grid[i][0]=0
        
        # Adding adjacent numbers.
        if grid[i][3]==grid[i][2]:
            grid[i][3]=grid[i][3]+grid[i][2]
            grid[i][2]=grid[i][1]
            grid[i][1]=grid[i][0]
            grid[i][0]=0
        if grid[i][2]==grid[i][1]:
            grid[i][2]=grid[i][2]+grid[i][1]
            grid[i][1]=grid[i][0]
            grid[i][0]=0
        if grid[i][1]==grid[i][0]:
            grid[i][1]=grid[i][1]+grid[i][0]
            grid[i][0]=0
               
def push_up(grid):
    
    # Pushing values upwards for every possible scenario.
    for i in range(4): 
        if grid[0][i]==0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]==0:
            pass
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]!=0:
            pass
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]==0:
            pass
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]==0:
            pass
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]==0:
            pass
        elif grid[0][i]==0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]!=0:
            grid[0][i]=grid[3][i] 
            grid[3][i]=0
        elif grid[0][i]==0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]!=0:
            grid[0][i]=grid[2][i] 
            grid[1][i]=grid[3][i] 
            grid[2][i]=0 
            grid[3][i]=0
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]!=0:
            grid[0][i]=grid[1][i] 
            grid[1][i]=grid[2][i] 
            grid[2][i]=grid[3][i] 
            grid[3][i]=0
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]==0:
            grid[1][i]=grid[2][i] 
            grid[2][i]=0 
            grid[3][i]=0
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]!=0:
            grid[0][i]=grid[1][i] 
            grid[1][i]=grid[3][i] 
            grid[2][i]=0 
            grid[3][i]=0
        elif grid[0][i]==0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]==0:
            grid[0][i]=grid[2][i] 
            grid[1][i]=0 
            grid[2][i]=0 
            grid[3][i]=0
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]==0:
            grid[0][i]=grid[1][i] 
            grid[0][i]=0 
            grid[0][i]=0 
            grid[0][i]=0
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]!=0:
            grid[1][i]=grid[3][i] 
            grid[2][i]=0 
            grid[3][i]=0
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]==0:
            grid[0][i]=grid[1][i] 
            grid[1][i]=grid[2][i] 
            grid[2][i]=0 
            grid[3][i]=0
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]!=0:
            grid[1][i]=grid[2][i] 
            grid[2][i]=grid[3][i] 
            grid[3][i]=0
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]!=0:
            grid[2][i]=grid[3][i] 
            grid[3][i]=0
                
        # Adding adjacent numbers.
        if grid[0][i]==grid[1][i]:
            grid[0][i]=grid[0][i]+grid[1][i]
            grid[1][i]=grid[2][i]
            grid[2][i]=grid[3][i]
            grid[3][i]=0
        if grid[1][i]==grid[2][i]:
            grid[1][i]=grid[1][i]+grid[2][i]
            grid[2][i]=grid[3][i]
            grid[3][i]=0
        if grid[2][i]==grid[3][i]:
            grid[2][i]=grid[2][i]+grid[3][i]
            grid[3][i]=0

def push_down(grid):
    
    # Pushing values downwards for every possible scenario.
    for i in range(4): 
        if grid[0][i]==0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]==0:
            pass
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]!=0:
            pass
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]==0:
            grid[3][i]=grid[0][i]
            grid[0][i]=0
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]==0:
            grid[3][i]=grid[1][i]
            grid[2][i]=grid[0][i]
            grid[0][i]=0
            grid[1][i]=0
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]==0:
            grid[3][i]=grid[2][i]
            grid[2][i]=grid[1][i]
            grid[1][i]=grid[0][i]
            grid[0][i]=0
        elif grid[0][i]==0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]!=0:
            pass
        elif grid[0][i]==0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]!=0:
            pass
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]!=0:
            pass
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]==0:
            grid[3][i]=grid[2][i]
            grid[2][i]=grid[0][i]
            grid[0][i]=0
            grid[1][i]=0 
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]!=0:
            grid[2][i]=grid[1][i]
            grid[0][i]=0 
            grid[1][i]=0 
        elif grid[0][i]==0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]==0:
            grid[3][i]=grid[2][i]
            grid[0][i]=0 
            grid[1][i]=0 
            grid[2][i]=0 
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]==0:
            grid[3][i]=grid[1][i]
            grid[0][i]=0 
            grid[1][i]=0 
            grid[2][i]=0 
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]==0 and grid[3][i]!=0:
            grid[2][i]=grid[0][i] 
            grid[0][i]=0
            grid[1][i]=0
        elif grid[0][i]==0 and grid[1][i]!=0 and grid[2][i]!=0 and grid[3][i]==0:
            grid[3][i]=grid[2][i]
            grid[2][i]=grid[1][i]
            grid[0][i]=0 
            grid[1][i]=0 
        elif grid[0][i]!=0 and grid[1][i]==0 and grid[2][i]!=0 and grid[3][i]!=0:
            grid[1][i]=grid[0][i]
            grid[0][i]=0
        elif grid[0][i]!=0 and grid[1][i]!=0 and grid[2][i]==0 and grid[3][i]!=0:
            grid[2][i]=grid[1][i]
            grid[1][i]=grid[0][i]
            grid[0][i]=0
            
        # Adding adjacent numbers.
        if grid[3][i]==grid[2][i]:
            grid[3][i]=grid[3][i]+grid[2][i]
            grid[2][i]=grid[1][i]
            grid[1][i]=grid[0][i]
            grid[0][i]=0
        if grid[2][i]==grid[1][i]:
            grid[2][i]=grid[2][i]+grid[1][i]
            grid[1][i]=grid[0][i]
            grid[0][i]=0
        if grid[1][i]==grid[0][i]:
            grid[1][i]=grid[1][i]+grid[0][i]
            grid[0][i]=0