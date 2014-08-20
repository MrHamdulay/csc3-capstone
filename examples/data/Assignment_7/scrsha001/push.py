#Shaaheen Sacoor SCRSHA001
#29 April 2014
#Functions to push a grid up,down,left or right for the 2048

def push_up(grid):
    for a in range(4): #Goes through columns
        #Checks if all grid values in a vertical row are empty
        if grid[0][a] ==0 and grid[1][a] ==0 and grid[2][a] ==0 and grid[3][a] ==0:
            pass #Do nothing if row is empty
        elif grid[0][a] ==0 and grid[1][a] ==0 and grid[2][a] ==0: 
            grid[0][a] = grid[3][a]    #Checks if there are 3 spaces from top
            grid[3][a] = 0             # adjusts appropiately
        elif grid[0][a] ==0 and grid[1][a] ==0:
            grid[0][a] = grid[2][a] #Checks if there are 2 spaces from top
            grid[1][a] = grid[3][a] #adjusts appropiately
            grid[2][a] = 0
            grid[3][a] = 0
            if grid[0][a] == grid[1][a]: #Adjacent values added
                grid[0][a] = grid[0][a]+grid[1][a]
                grid[1][a] =0
        elif grid[0][a] ==0 :
            grid[0][a] = grid[1][a] #Checks if there is 1 spaces from top
            grid[1][a] = grid[2][a] #adjusts appropiately
            grid[2][a] = grid[3][a]
            grid[3][a] =0
            if grid[1][a] == 0:       #Adjacent values added
                grid[1][a] = grid[2][a]
                grid[2][a] = 0
            if grid[0][a] == grid[1][a]:
                grid[0][a] =grid[0][a]+grid[1][a]
                grid[1][a] = grid[2][a]
                grid[2][a] =0
            if grid[1][a] ==grid[2][a]:
                grid[1][a] = grid[1][a] + grid[2][a]
                grid[2][a] =0
        else:           #goes through column and adjusts for when the top grid value
            if grid[1][a] == 0 and grid[2][a] ==0 and grid[3][a] ==0: #is not empty
                pass
            elif grid[1][a] ==0 and grid[2][a] ==0:
                grid[1][a] =grid[3][a]
                grid[3][a] = 0
            elif grid[1][a] ==0:
                grid[1][a] =grid[2][a]
                grid[2][a] =grid[3][a]
                grid[3][a] =0
            elif grid[2][a] ==0 and grid[3][a] ==0:
                pass
            elif grid[2][a] ==0:
                grid[2][a] =grid[3][a]
                grid[3][a] =0
            elif grid[3][a] ==0:
                pass
            if grid[0][a] ==grid[1][a]: #Adjacent values added
                grid[0][a] = grid[0][a] + grid[1][a]
                grid[1][a] =grid[2][a]
                grid[2][a] = grid[3][a]
                grid[3][a] =0
            if grid[1][a] ==grid[2][a]:
                grid[1][a] =grid[1][a] +grid[2][a]
                grid[2][a] =grid[3][a]
                grid[3][a] =0
            if grid[2][a] == grid[3][a]:
                grid[2][a] = grid[2][a]+grid[3][a]
                grid[3][a]=0
def push_down(grid): #Same as push_up but you would start from the top and go down
    for a in range(4): #Positions are opposite to push_up
        if grid[3][a] ==0 and grid[2][a] ==0 and grid[1][a] ==0 and grid[0][a] ==0:
            pass
        elif grid[3][a] ==0 and grid[2][a] ==0 and grid[1][a] ==0:
            grid[3][a] = grid[0][a]
            grid[0][a] = 0
        elif grid[3][a] ==0 and grid[2][a] ==0:
            grid[3][a] = grid[1][a]
            grid[2][a] = grid[0][a]
            grid[1][a] = 0
            grid[0][a] = 0
            if grid[3][a] == grid[2][a]:
                grid[3][a] = grid[3][a]+grid[2][a]
                grid[2][a] =0
        elif grid[3][a] ==0 :
            grid[3][a] = grid[2][a]
            grid[2][a] = grid[1][a]
            grid[1][a] = grid[0][a]
            grid[0][a] =0
            if grid[2][a] == 0:
                grid[2][a] = grid[1][a]
                grid[1][a] = 0
            if grid[3][a] == grid[2][a]:
                grid[3][a] =grid[3][a]+grid[2][a]
                grid[2][a] = grid[1][a]
                grid[1][a] =0
            if grid[2][a] ==grid[1][a]:
                grid[2][a] = grid[2][a] + grid[1][a]
                grid[1][a] =0
        else:
            if grid[2][a] == 0 and grid[1][a] ==0 and grid[0][a] ==0:
                pass
            elif grid[2][a] ==0 and grid[1][a] ==0:
                grid[2][a] =grid[0][a]
                grid[0][a] = 0
            elif grid[2][a] ==0:
                grid[2][a] =grid[1][a]
                grid[1][a] =grid[0][a]
                grid[0][a] =0
            elif grid[1][a] ==0 and grid[0][a] ==0:
                pass
            elif grid[1][a] ==0:
                grid[1][a] =grid[0][a]
                grid[0][a] =0
            elif grid[0][a] ==0:
                pass
            if grid[3][a] ==grid[2][a]:
                grid[3][a] = grid[3][a] + grid[2][a]
                grid[2][a] =grid[1][a]
                grid[1][a] = grid[0][a]
                grid[0][a] =0
            if grid[2][a] ==grid[1][a]:
                grid[2][a] =grid[2][a] +grid[1][a]
                grid[1][a] =grid[0][a]
                grid[0][a] =0
            if grid[1][a] == grid[0][a]:
                grid[1][a] = grid[1][a]+grid[0][a]
                grid[0][a]=0
                
def push_left(grid): #Same as push_up but will now check rows not columns 
                     #and adjusts accordingly
    ng = grid
    for i in range(4):
        for x in range(4):
            if grid[i][x] == " ":
                grid[i][x] = 0

    for a in range(4):
        if ng[a][0] ==0 and ng[a][1] ==0 and ng[a][2] ==0 and ng[a][3] ==0:
            pass
        elif ng[a][0] ==0 and ng[a][1] ==0 and ng[a][2] ==0:
            ng[a][0] = ng[a][3]
            ng[a][3] = 0
        elif ng[a][0] ==0 and ng[a][1] ==0:
            ng[a][0] = ng[a][2]
            ng[a][1] = ng[a][3]
            ng[a][2] = 0
            ng[a][3] = 0
            if ng[a][0] == ng[a][1]:
                ng[a][0] = ng[a][0]+ng[a][1]
                ng[a][1] =0
        elif ng[a][0] ==0 :
            ng[a][0] = ng[a][1]
            ng[a][1] = ng[a][2]
            ng[a][2] = ng[a][3]
            ng[a][3] =0
            if ng[a][1] == 0:
                ng[a][1] = ng[a][2]
                ng[a][2] = 0
            if ng[a][0] == ng[a][1]:
                ng[a][0] =ng[a][0]+ng[a][1]
                ng[a][1] = ng[a][2]
                ng[a][2] =0
            if ng[a][1] ==ng[a][2]:
                ng[a][1] = ng[a][1] + ng[a][2]
                ng[a][2] =0
        else:
            if ng[a][1] == 0 and ng[a][2] ==0 and ng[a][3] ==0:
                pass
            elif ng[a][1] ==0 and ng[a][2] ==0:
                ng[a][1] =ng[a][3]
                ng[a][3] = 0
            elif ng[a][1] ==0:
                ng[a][1] =ng[a][2]
                ng[a][2] =ng[a][3]
                ng[a][3] =0
            elif ng[a][2] ==0 and ng[a][3] ==0:
                pass
            elif ng[a][2] ==0:
                ng[a][2] =ng[a][3]
                ng[a][3] =0
            elif ng[a][3] ==0:
                pass
            if ng[a][0] ==ng[a][1]:
                ng[a][0] = ng[a][0] + ng[a][1]
                ng[a][1] =ng[a][2]
                ng[a][2] = ng[a][3]
                ng[a][3] =0
            if ng[a][1] ==ng[a][2]:
                ng[a][1] =ng[a][1] +ng[a][2]
                ng[a][2] =ng[a][3]
                ng[a][3] =0
            if ng[a][2] == ng[a][3]:
                ng[a][2] = ng[a][2]+ng[a][3]
                ng[a][3]=0
                
    
   
def push_right(grid):
    #Same as push_down but will now check rows not columns 
                         #and adjusts accordingly    
    ng = grid
    for i in range(4):
        for x in range(4):
            if grid[i][x] == " ":
                grid[i][x] = 0
    for a in range(4):
        if ng[a][0] ==0 and ng[a][1] ==0 and ng[a][2] ==0 and ng[a][3] ==0:
            pass
        elif ng[a][3] ==0 and ng[a][2] ==0 and ng[a][1] ==0:
            ng[a][3] = ng[a][0]
            ng[a][0] = 0
        elif ng[a][3] ==0 and ng[a][2] ==0:
            ng[a][3] = ng[a][1]
            ng[a][2] = ng[a][0]
            ng[a][1] = 0
            ng[a][0] = 0
            if ng[a][3] == ng[a][2]:
                ng[a][3] = ng[a][3]+ng[a][2]
                ng[a][2] =0
        elif ng[a][3] ==0 :
            ng[a][3] = ng[a][2]
            ng[a][2] = ng[a][1]
            ng[a][1] = ng[a][0]
            ng[a][0] =0
            if ng[a][2] == 0:
                ng[a][2] = ng[a][1]
                ng[a][1] = 0
            if ng[a][3] == ng[a][2]:
                ng[a][3] =ng[a][3]+ng[a][2]
                ng[a][2] = ng[a][1]
                ng[a][1] =0
            if ng[a][2] ==ng[a][1]:
                ng[a][2] = ng[a][1] + ng[a][2]
                ng[a][1] =0
        else:
            if ng[a][2] == 0 and ng[a][1] ==0 and ng[a][0] ==0:
                pass
            elif ng[a][1] ==0 and ng[a][2] ==0:
                ng[a][2] =ng[a][0]
                ng[a][0] = 0
            elif ng[a][2] ==0:
                ng[a][2] =ng[a][1]
                ng[a][1] =ng[a][0]
                ng[a][0] =0
            elif ng[a][1] ==0 and ng[a][0] ==0:
                pass
            elif ng[a][1] ==0:
                ng[a][1] =ng[a][0]
                ng[a][0] =0
            elif ng[a][0] ==0:
                pass
            if ng[a][3] ==ng[a][2]:
                ng[a][3] = ng[a][3] + ng[a][2]
                ng[a][2] =ng[a][1]
                ng[a][1] = ng[a][0]
                ng[a][0] =0
            if ng[a][2] ==ng[a][1]:
                ng[a][2] =ng[a][2] +ng[a][1]
                ng[a][1] =ng[a][0]
                ng[a][0] =0
            if ng[a][0] ==ng[a][1]:
                ng[a][1] =ng[a][0] +ng[a][1]
                ng[a][0] =0
    
