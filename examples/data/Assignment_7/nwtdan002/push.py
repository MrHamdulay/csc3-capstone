'''Program to take pushnumbers around in a grid, combining them if two of the same number come into contact
By Daniel Newton
27/04/14'''

def push_up(grid):      #movement of numbers in grid up
    for a in range(4):
        for b in range(3):
            row=b+1
            while grid[b][a]==0:    #gets rid of spaces between numbers and compresses then upwards
                grid[b][a]=grid[row][a]
                grid[row][a]=0
                row+=1
                if row==4:
                    break                    
        for b in range(3):          #combines numbers that are vertically adjacent, moving the lower number up.
            if grid[b][a]==grid[b+1][a]:
                grid[b][a]*=2
                grid[b+1][a]=0
            
            row=b+1
            while grid[b][a]==0:    #gets rid of remaining spaces in the same way as previously
                grid[b][a]=grid[row][a]
                grid[row][a]=0
                row+=1
                if row==4:
                    break

def push_down(grid):      #movement of numbers in grid down
    for a in range(4):
        for b in range(3,0,-1):
            row=b
            while grid[b][a]==0:    #gets rid of spaces between numbers and compresses then downwards
                grid[b][a]=grid[row][a]
                grid[row][a]=0
                row-=1
                if row==-1:
                    break                    
        for b in range(3,0,-1):          #combines numbers that are vertically adjacent, moving the upper number down.
            if grid[b][a]==grid[b-1][a]:
                grid[b][a]*=2
                grid[b-1][a]=0
            
            row=b
            while grid[b][a]==0:    #gets rid of remaining spaces in the same way as previously
                grid[b][a]=grid[row][a]
                grid[row][a]=0
                row-=1
                if row==-1:
                    break

def push_left(grid):      #movement of numbers in grid left
    for b in range(4):
        for a in range(3):
            column=a+1
            while grid[b][a]==0:    #gets rid of spaces between numbers and compresses then left
                grid[b][a]=grid[b][column]
                grid[b][column]=0
                column+=1
                if column==4:
                    break                    
        for a in range(3):          #combines numbers that are horizontally adjacent, moving the right number to the left.
            if grid[b][a]==grid[b][a+1]:
                grid[b][a]*=2
                grid[b][a+1]=0
            
            column=a+1
            while grid[b][a]==0:    #gets rid of remaining spaces in the same way as previously
                grid[b][a]=grid[b][column]
                grid[b][column]=0
                column+=1
                if column==4:
                    break
                
def push_right(grid):      #movement of numbers in grid right
    for b in range(4):
        for a in range(3,0,-1):
            column=a
            while grid[b][a]==0:    #gets rid of spaces between numbers and compresses then right
                grid[b][a]=grid[b][column]
                grid[b][column]=0
                column-=1
                if column==-1:
                    break                    
        for a in range(3,0,-1):          #combines numbers that are horizontally adjacent, moving the left number to the right.
            if grid[b][a]==grid[b][a-1]:
                grid[b][a]*=2
                grid[b][a-1]=0
            
            column=a
            while grid[b][a]==0:    #gets rid of remaining spaces in the same way as previously
                grid[b][a]=grid[b][column]
                grid[b][column]=0
                column-=1
                if column==-1:
                    break