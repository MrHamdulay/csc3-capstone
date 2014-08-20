"""Module of Functions to merge numbers in a confined grid"""
#Liam Brodie
#BRDLIA004          
#April 2014

import util

def push_up (grid):
    """merge grid values upwards"""
    newGrid = util.copy_grid (grid)
    for Column in range(4):
        ListColumn = []
        for Row in range(4):
            ListColumn.append(grid[Row][Column])
            
        for p in range(3):
            for Row in range(4):
                if (Row!=3 and ListColumn[Row]==0):
                
                    for i in range(Row,3):
                        ListColumn[i]=ListColumn[i+1]
                        ListColumn[i+1]=0
        for Row in range(4):            
            if (Row!=3 and ListColumn[Row]==ListColumn[Row+1]):
                ListColumn[Row]+=ListColumn[Row+1]
                ListColumn[Row+1]=0
                for i in range(Row+1, 3):
                    ListColumn[i]=ListColumn[i+1]
                    ListColumn[i+1]=0           
            for Row in range(4):
                grid[Row][Column]=ListColumn[Row]
    

def push_down (grid):
    """merge grid values downwards"""
    newGrid = util.copy_grid (grid)
    
    for Column in range(4):
        ListColumn = []
        for Row in range(4):
      
            ListColumn.append(grid[Row][Column])
        for p in range(3):
            for Row in range(3,0,-1):
                if (Row!=0 and ListColumn[Row]==0):
                    
                    for i in range(Row,0,-1):
                        ListColumn[i]=ListColumn[i-1]
                        ListColumn[i-1]=0
        for Row in range(3,0,-1):            
            if (Row!=0 and ListColumn[Row]==ListColumn[Row-1]):
                ListColumn[Row]+=ListColumn[Row-1]
                ListColumn[Row-1]=0
                
                for i in range(Row-1, 0,-1):
                    ListColumn[i]=ListColumn[i-1]
                    ListColumn[i-1]=0
            for Row in range(4):
                grid[Row][Column]=ListColumn[Row]
    
    if(newGrid!=grid):
        push_down(grid) 
        

def push_left (grid):
    """merge grid values left"""
    newGrid = util.copy_grid (grid)
    
    for Row in range(4):
        ListRow = []
        for Column in range(4):
    
            ListRow.append(grid[Row][Column])      
        for p in range(3):    
            for Column in range(4):
                if (Column!=3 and ListRow[Column]==0):
                    
                    for i in range(Column, 3):
                        ListRow[i]=ListRow[i+1]
                        ListRow[i+1]=0
        for Column in range(4):            
            if (Column!=3 and ListRow[Column]==ListRow[Column+1]):
                ListRow[Column]+=ListRow[Column+1]
                ListRow[Column+1]=0
                for i in range(Column+1, 3):
                    ListRow[i]=ListRow[i+1]
                    ListRow[i+1]=0                
                        
         
            for Column in range(4):
                grid[Row][Column]=ListRow[Column]


def push_right (grid):
    """merge grid values right"""   
    newGrid = util.copy_grid (grid)
    
    for Row in range(4):
        ListRow = []
        for Column in range(4):
            ListRow.append(grid[Row][Column])
        for p in range(3):    
            for Column in range(3,0,-1):
                if (Column!=0 and ListRow[Column]==0):
                    
                    for i in range(Column, 0,-1):
                        ListRow[i]=ListRow[i-1]
                        ListRow[i-1]=0
        for Column in range(3,0,-1):            
            if (Column!=0 and ListRow[Column]==ListRow[Column-1]):
                ListRow[Column]+=ListRow[Column-1]
                ListRow[Column-1]=0
                for i in range(Column-1, 0,-1):
                    ListRow[i]=ListRow[i-1]
                    ListRow[i-1]=0
                
            for Column in range(4):
                grid[Row][Column]=ListRow[Column]
    
    if(newGrid!=grid):
        push_right(grid)     