"""Module to merge grid values when moved in a certain direction
B.Player
27/04/2014"""
import util

def push_up(grid):
   """merge grid values upwards"""
   #storing numbers in temp array
   for col in range(4):
      line=[]
      for row in range(4):         
         line.append(grid[row][col])
      #moving numbers in temp array
      for i in range(4):
         if 0 in line:
            line.remove(0)
            
      #replacing removed indexes to get 4 columns again
      length=len(line)
      for i in range(4-length):
         line.append(0)
    
      #copying numbers back to grid
      for row in range(4):
         grid[row][col]=line[row]

#----------------------------------------------
         
   for col in range(4):
      temp=[]
      for row in range(4):         
         temp.append(grid[row][col])
      
      #merging numbers in temp array
      for i in range(3):
         if temp[i]==temp[i+1]:
            x=temp[i+1]            
            temp[i]=x*2
            temp[i+1]=0
            
      #moving numbers in temp array
      for i in range(4):
         if 0 in temp:
            temp.remove(0)      
      
      length=len(temp)
      for i in range(4-length):
         temp.append(0)  

      
      #copying numbers back to grid
      for row in range(4):
         grid[row][col]=temp[row]         
         

def push_down(grid):
   """merge grid values downwards"""
   #storing numbers in temp array
   for col in range(4):
      line=[]
      for row in range(4):         
         line.append(grid[row][col])
      line.reverse() # reversing order so zeros are removed from bottom up
      #moving numbers in temp array
      for i in range(4):
         if 0 in line:
            line.remove(0)
            
      #replacing removed indexes to get 4 columns again
      length=len(line)
      for i in range(4-length):
         line.append(0)
      line.reverse() #reversing again to get original order
      #copying numbers back to grid
      for row in range(4):
         grid[row][col]=line[row]   
#----------------------------------------------
         
   for col in range(4):
      temp=[]
      for row in range(4):         
         temp.append(grid[row][col])
      temp.reverse() #reversing so zeros are removed from right to left
      #merging numbers in temp array
      for i in range(3):
         if temp[i]==temp[i+1]:
            x=temp[i+1]            
            temp[i]=x*2
            temp[i+1]=0
            
      #moving numbers in temp array
      for i in range(4):
         if 0 in temp:
            temp.remove(0)      
      
      length=len(temp)
      for i in range(4-length):
         temp.append(0)  

      temp.reverse() #reversing to get back to original order
      #copying numbers back to grid
      for row in range(4):
         grid[row][col]=temp[row]             

def push_left(grid):
   """merge grid values left"""   
   #storing numbers in temp array
   for row in range(4):
      line=[]
      for col in range(4):         
         line.append(grid[row][col])
      #moving numbers in temp array
      for i in range(4):
         if 0 in line:
            line.remove(0)
            
      #Replacing removed indexes with 0
      length=len(line)
      for i in range(4-length):
         line.append(0)  
      
      #copying numbers back to grid
      for col in range(4):
         grid[row][col]=line[col]
 #---------------------------------------------------------- 
   for row in range(4):
      temp=[]
      for col in range(4):         
         temp.append(grid[row][col])
      
      #merging numbers in temp array
      for i in range(3):
         if temp[i]==temp[i+1]:
            x=temp[i+1]            
            temp[i]=x*2
            temp[i+1]=0
            
      #moving numbers in temp array
      for i in range(4):
         if 0 in temp:
            temp.remove(0)      
      
      length=len(temp)
      for i in range(4-length):
         temp.append(0)  

      
      #copying numbers back to grid
      for col in range(4):
         grid[row][col]=temp[col]        
            

def push_right(grid):
   """merge grid values right"""
   #storing numbers in temp array
   for row in range(4):
      line=[]
      for col in range(4):         
         line.append(grid[row][col])
      line.reverse() #reversing so zeros are removed from right to left
      #moving numbers in temp array
      for i in range(4):
         if 0 in line:
            line.remove(0)

      length=len(line)
      for i in range(4-length):
         line.append(0)  
      line.reverse() #reversing again to get original order
      #copying numbers back to grid
      for col in range(4):
         grid[row][col]=line[col]   
      
 #---------------------------------------------------------- 
   for row in range(4):
      temp=[]
      for col in range(4):         
         temp.append(grid[row][col])
      temp.reverse() #reversing so zeros are removed from right to left
      #merging numbers in temp array
      for i in range(3):
         if temp[i]==temp[i+1]:
            x=temp[i+1]            
            temp[i]=x*2
            temp[i+1]=0
            
      #moving numbers in temp array
      for i in range(4):
         if 0 in temp:
            temp.remove(0)      
      
      length=len(temp)
      for i in range(4-length):
         temp.append(0)  

      temp.reverse() #reversing so zeros are removed from right to left
      #copying numbers back to grid
      for col in range(4):
         grid[row][col]=temp[col]         