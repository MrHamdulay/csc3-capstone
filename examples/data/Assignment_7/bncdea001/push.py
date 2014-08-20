#Module for pushing tiles in 2048
#Dean Bunce
#26 April 2014


def push_up(grid):
   
   #Remove all spaces from top to bottom
   for i in range(3): 
      for row in range(3):
         for column in range(4):
            
            if grid[row][column]==0:
               
               grid[row][column]=grid[row+1][column]
               
               grid[row+1][column]=0
               
               
   #Add adjacent values from top to bottom
   for row in range(3):
      for column in range(4):
            
         if grid[row][column]==grid[row+1][column]:
               
            grid[row][column]=grid[row][column]+grid[row+1][column]
               
            grid[row+1][column]=0
            
   #Remove all spaces from top to bottom
   for i in range(3): 
         for row in range(3):
               for column in range(4):
                          
                  if grid[row][column]==0:
                             
                     grid[row][column]=grid[row+1][column]
                             
                     grid[row+1][column]=0      

def push_down(grid):
   
   #Reverse direction and remove spaces (from bottom to top)
   for i in range(3):
      for row in range(3,0,-1):
         column=0
         while column<=3:
            
            
            
            if grid[row][column]==0:
               
               grid[row][column]=grid[row-1][column]
               
               grid[row-1][column]=0
               
            column+=1
   
   #Add adjacent values from bottom to top
   for row in range(3,0,-1):
      column=0
      while column<=3:
            
         if grid[row][column]==grid[row-1][column]:
               
            grid[row][column]=grid[row][column]+grid[row-1][column]
               
            grid[row-1][column]=0
               
       
       
         column=column+1
          
    #Remove all spaces from bottom to top
   for i in range(3):
      for row in range(3,0,-1):
         column=0
         while column<=3:
                           
            if grid[row][column]==0:
                              
               grid[row][column]=grid[row-1][column]
                              
               grid[row-1][column]=0
            column+=1

def push_left(grid):
   
   #Remove all empty spaces from left to right
   for i in range(3):
      for row in range(4):
         for column in range(3):
            
            if grid[row][column]==0:
               
               grid[row][column]=grid[row][column+1]
               
               grid[row][column+1]=0
               
   #Add adjacent values from left to right
   for row in range(4):
      for column in range(3):
           
         if grid[row][column]==grid[row][column+1]:
            
            grid[row][column]=grid[row][column]+grid[row][column+1]
               
            grid[row][column+1]=0
            
            
   #Remove all spaces from left to right         
   for i in range(3):
      for row in range(4):
         for column in range(3):
                           
            if grid[row][column]==0:
                              
               grid[row][column]=grid[row][column+1]
                              
               grid[row][column+1]=0
               

def push_right(grid):
   
   #Remove all spaces from right to left
   for i in range(3):
      for row in range(4):
         for column in range(3,0,-1):
            
            if grid[row][column]==0:
               
               grid[row][column]=grid[row][column-1]
               
               grid[row][column-1]=0
               
   #Add adjacent values from right to left
   for row in range(4):
      for column in range(3,0,-1):
            
         if grid[row][column]==grid[row][column-1]:
               
            grid[row][column]=grid[row][column]+grid[row][column-1]
               
            grid[row][column-1]=0
            
   #Remove all spaces from right to left       
   for i in range(3):
      for row in range(4):
            for column in range(3,0,-1):
                           
               if grid[row][column]==0:
                              
                  grid[row][column]=grid[row][column-1]
                              
                  grid[row][column-1]=0      
                  
               