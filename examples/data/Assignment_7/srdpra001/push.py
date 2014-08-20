'''
Prashanth Sridharan
SRDPRA001
Assignment 07
Question 3
'''
def push_up (grid): 
    for a in range (4): 
        for p in range(3,0,-1):
            for q in range(4):
                if grid[p-1][q]==0:
                    grid[p-1][q]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(3): 
        for q in range(4):      
            if grid[p][q]==grid[p+1][q]:
                grid[p][q]=(grid[p][q])*2
                grid[p+1][q]=0
               
    for a in range (4): #push the values up to their maximum heights after the combining
        for p in range(3,0,-1):
            for q in range(4):
                if grid[p-1][q]==0:
                    grid[p-1][q]=grid[p][q]
                    grid[p][q]=0 

def push_down (grid): 
    for a in range(4): 
        for p in range(2,-1,-1):
            for q in range(4):
                if grid[p+1][q]==0:
                    grid[p+1][q]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(2,-1,-1):
        for q in range(4):
            if grid[p][q]==grid[p+1][q]:
                grid[p+1][q]=(grid[p+1][q])*2
                grid[p][q]=0
                
    for a in range(4): #push the values down to their minimum heights after the combining
        for p in range(2,-1,-1):
            for q in range(4):
                if grid[p+1][q]==0:
                    grid[p+1][q]=grid[p][q]
                    grid[p][q]=0   
                    
def push_left (grid): 
    for a in range(4):
        for p in range(4): 
            for q in range(3,0,-1): 
                if grid[p][q-1]==0:
                    grid[p][q-1]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(4):
        for q in range(3): 
            if grid[p][q]==grid[p][q+1]:
                grid[p][q]=(grid[p][q])*2
                grid[p][q+1]=0    
                                   
    for a in range(4): #push the values left to the extreme left after the combining
        for p in range(4): 
            for q in range(3,0,-1): 
                if grid[p][q-1]==0:
                    grid[p][q-1]=grid[p][q]
                    grid[p][q]=0
            
def push_right (grid):  
    for a in range(4):
        for p in range(4):
            for q in range(3): 
                if grid[p][q+1]==0:
                    grid[p][q+1]=grid[p][q]
                    grid[p][q]=0
                    
    for p in range(4): #push the values right to the extreme right after the combining
            for q in range(3,0,-1): 
                if grid[p][q]==grid[p][q-1]:
                    grid[p][q]=(grid[p][q])*2
                    grid[p][q-1]=0
                    
    for a in range(4):
        for p in range(4):
            for q in range(3): 
                if grid[p][q+1]==0:
                    grid[p][q+1]=grid[p][q]
                    grid[p][q]=0    