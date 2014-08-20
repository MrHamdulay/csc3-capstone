#Soham Singh
#SNGSOH004
#Assignment 7
#Question 3 - push.py

def push_up (grid): 
    
    for a in range (0,4): 
        
        for p in range(3,0,-1):
            
            for q in range(0,4):
                
                if grid[p-1][q]==0: #if there is an empty space, then shift the non-zero value to that space
                    grid[p-1][q]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(0,3): 
        
        for q in range(0,4): 
            
            if grid[p][q]==grid[p+1][q]: #if the adjacent values are equal, then merge them
                grid[p][q]=grid[p][q]*2
                grid[p+1][q]=0
               
    for a in range (0,4): #to shift all merged values into their furthest position possible
        
        for p in range(3,0,-1):
            
            for q in range(0,4):
                
                if grid[p-1][q]==0:
                    grid[p-1][q]=grid[p][q]
                    grid[p][q]=0 

def push_down (grid): 
    
    for a in range(0,4): 
        
        for p in range(2,-1,-1):
            
            for q in range(0,4):
                
                if grid[p+1][q]==0: #if there is an empty space, then shift the non-zero value to that space
                    grid[p+1][q]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(2,-1,-1):
        
        for q in range(0,4):
            
            if grid[p][q]==grid[p+1][q]: #if the adjacent values are equal, then merge them
                grid[p+1][q]=(grid[p+1][q])*2
                grid[p][q]=0
                
    for a in range(0,4):  #to shift all merged values into their furthest position possible
        
        for p in range(2,-1,-1):
            
            for q in range(0,4):
                
                if grid[p+1][q]==0:
                    grid[p+1][q]=grid[p][q]
                    grid[p][q]=0   
                    
def push_left (grid): 
    
    for a in range(0,4):
        
        for p in range(0,4): 
            
            for q in range(3,0,-1): 
                
                if grid[p][q-1]==0: #if there is an empty space, then shift the non-zero value to that space
                    grid[p][q-1]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(0,4):
        
        for q in range(0,3): 
            
            if grid[p][q]==grid[p][q+1]: #if the adjacent values are equal, then merge them
                grid[p][q]=(grid[p][q])*2
                grid[p][q+1]=0    
                                   
    for a in range(0,4): #to shift all merged values into their furthest position possible
        
        for p in range(0,4): 
            
            for q in range(3,0,-1): 
                
                if grid[p][q-1]==0:
                    grid[p][q-1]=grid[p][q]
                    grid[p][q]=0
            
def push_right (grid):  
    
    for a in range(0,4):
        
        for p in range(0,4):
            
            for q in range(0,3): 
                
                if grid[p][q+1]==0: #if there is an empty space, then shift the non-zero value to that space
                    grid[p][q+1]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(0,4): 
        
            for q in range(3,0,-1): 
                
                if grid[p][q]==grid[p][q-1]: #if the adjacent values are equal, then merge them
                    grid[p][q]=(grid[p][q])*2
                    grid[p][q-1]=0
                    
    for a in range(0,4): #to shift all merged values into their furthest position possible
        
        for p in range(0,4):
            
            for q in range(0,3): 
                
                if grid[p][q+1]==0:
                    grid[p][q+1]=grid[p][q]
                    grid[p][q]=0    