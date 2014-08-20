#ashton


def push_up (block):
    """merge grid values upwards"""
    for a in range (3):
        for b in range(3):
            for c in range(4): 
                if block[b][c] == 0: 
                    block[b][c] = block[b+1][c]
                    block[b+1][c] = 0
    
    for b in range(3):
        for c  in range (4):
            if block[b][c] == block[b+1][c]: 
                block[b][c] *= 2 
                block[b+1][c] = 0 
         
           
    for a in range (3):
        for b in range(3):
            for c in range(4):
                if block[b][c] == 0:
                    block[b][c] = block[b+1][c]
                    block[b+1][c] = 0                

def push_down (block):
    """merge grid values downwards"""
    for a in range (3):
        for b in range(3):
            for c in range(4):
                 
                if (block[b+1][c] == 0):
                 
                    block[b+1][c] = block[b][c]
                    
                    block[b][c] = 0
                
    for b in range(3, 0, -1):
        for c  in range (4):
            
            if block[b][c] == block[b-1][c]:
            
                block[b][c] *= 2
                
                block[b-1][c] = 0  
          
                 
    for a in range (3):
        for b in range(3):
            for c in range(4):
                if (block[b+1][c] == 0):
                    block[b+1][c] = block[b][c]
                    block[b][c] = 0
                
def push_left (block):
    """merge grid values left"""
    for a in range (3):
        for b in range(4):
            for j in range(3):
                 
                if block[b][j] == 0:
                    
                    block[b][j] = block[b][j+1]
                    
                    block[b][j+1] = 0
                    
    for b in range(4):
        for j in range (3):
            
            if block[b][j] == block[b][j+1]:
                
                block[b][j] *= 2
                
                block[b][j+1] = 0
            
             
    for a in range (3):
        for b in range(4):
            for j in range(3):
                if block[b][j] == 0:
                    block[b][j] = block[b][j+1]
                    block[b][j+1] = 0    
    
  
def push_right (block):
    """merge grid values right"""
    for a in range (4):
        for b in range(4):
            for j in range(3, 0, -1):
                 
                if block[b][j] == 0: 
                    
                    block[b][j] = block[b][j-1] 
                    
                    block[b][j-1] = 0
                    
    for b in range(4):
        for j in range (3):
            
            if block[b][j] == block[b][j+1]:
                
                block[b][j] *= 2
                
                block[b][j+1] = 0
                
     
    for a in range (4):
        for b in range(4):
            for j in range(3, 0, -1):
                if block[b][j] == 0:
                    block[b][j] = block[b][j-1]
                    block[b][j-1] = 0  