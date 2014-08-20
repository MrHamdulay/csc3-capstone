"""push.py
Adam Edelberg
2014/04/29"""
    
section = []

def push_up (grid):
    """merge grid values upwards"""
    
    for row in range (4):
        section = []
        for col in range (4):
            section.append(grid[col][row])
        add(section)
        for i in range (4):
            grid[i][row] = section[i]
        

def push_down (grid):
    """merge grid values downwards"""
    
    for row in range (4):
        section = []
        for col in range (4):
            section.append(grid[3-col][row])
        add(section)
        for i in range (4):
            grid[i][row] = section[3-i]      

def push_left (grid):
    """merge grid values left"""
    
    for row in range (4):
        section = []
        for col in range (4):
            section.append(grid[row][col])
        add(section)
        for i in range (4):
            grid[row][i] = section[i]        
        
    

def push_right (grid):
    """merge grid values right"""     
    
    for row in range (4):
        section = []
        for col in range (4):
            section.append(grid[row][3-col])
        add(section) 
        for i in range (4):
            grid[row][i] = section[3-i]             
    


def remove_space (section):
    """[0,0,0,0]"""
    for i in range (1,4):
        for j in range (1,i+1):
            if section[i-j]== 0:
                section[i-j]=section[i-j+1]
                section[i-j+1] = 0
        
def add(section):
    remove_space(section)
    for i in range (3):
        if section[i] == section[i+1]:
            section[i]+= section[i+1]
            section[i+1] = 0
    remove_space(section)
