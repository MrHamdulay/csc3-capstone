"""2048 game
Michelle Lu
1 May 2014"""

def push_up(grid):
   for col in range(4):
      newlist=[] #create a new list of the columns
      for row in range(4):
         newlist.append(grid[row][col])
      
      if newlist.count(0)!=4: #checks that it's not all spaces

         while 0 in newlist: #checks for empty spaces
            newlist.remove(0) #deletes empty spaces
            
         for i in range(len(newlist)):

            if i<len(newlist)-1: 
               if newlist[i]==newlist[i+1]: #if number is equal to number to the right add them 
                  newlist[i]=newlist[i]*2
                  del newlist[i+1] #delete the number to the right
      secondlist=newlist
      while len(secondlist)<4: #make the length of the list the same length as the grid
         secondlist.append(0)
      grid[0][col]=secondlist[0] #place the new values in the grid
      grid[1][col]=secondlist[1]
      grid[2][col]=secondlist[2]
      grid[3][col]=secondlist[3]
   return grid
  
#push_up([[0,2,3,0],[0,0,3,0],[0,2,0,0],[0,0,3,0]])

def push_down(grid):
   for col in range(4):
      revlist=[] #create a new list of the columns
      for row in range(3,-1,-1):
         revlist.append(grid[row][col])
      if revlist.count(0)!=4:
      
         while 0 in revlist: #checks for empty spaces
            revlist.remove(0) #deletes empty spaces         
         
         for i in range(len(revlist)):
              
            if i<len(revlist)-1: 
               if revlist[i]==revlist[i+1]: #if number is equal to number to the right add them 
                  revlist[i]=revlist[i]*2
                  del revlist[i+1] #delete the number to the right           
      secondlist=revlist
      while len(secondlist)<4: #make the length of the list the same length as the grid
         secondlist.append(0)
      grid[0][col]=secondlist[3] #place the new values in the grid
      grid[1][col]=secondlist[2]
      grid[2][col]=secondlist[1]
      grid[3][col]=secondlist[0]
   return grid
 



def push_left(grid):
   for row in range(4):
      newlist=[] #create a new list of the rows
      for col in range(4):
         newlist.append(grid[row][col])
         
      if newlist.count(0)!=4:
         
         while 0 in newlist: #checks for empty spaces
            newlist.remove(0) #deletes empty spaces         
         
         for i in range(len(newlist)):
              
            if i<len(newlist)-1: 
               if newlist[i]==newlist[i+1]: #if number is equal to number to the right add them 
                  newlist[i]=newlist[i]*2
                  del newlist[i+1] #delete the number to the right            
      secondlist=newlist
      while len(secondlist)<4: #make the length of the list the same length as the grid
         secondlist.append(0)
      grid[row][0]=secondlist[0] #place the new values in the grid
      grid[row][1]=secondlist[1]
      grid[row][2]=secondlist[2]
      grid[row][3]=secondlist[3]
   return grid
  
 


def push_right(grid):
   for row in range(4):
      revlist=[] #create a new list of the rows
      for col in range(3,-1,-1):
         revlist.append(grid[row][col])
         
      if revlist.count(0)!=4:
         while 0 in revlist: #checks for empty spaces
            revlist.remove(0) #deletes empty spaces      
         for i in range(len(revlist)):
               
            if i<len(revlist)-1: 
               if revlist[i]==revlist[i+1]: #if number is equal to number to the right add them 
                  revlist[i]=revlist[i]*2
                  del revlist[i+1] #delete the number to the right      
      secondlist=revlist
      while len(secondlist)<4: #make the length of the list the same length as the grid
         secondlist.append(0)
      grid[row][0]=secondlist[3] #place the new values in the grid
      grid[row][1]=secondlist[2]
      grid[row][2]=secondlist[1]
      grid[row][3]=secondlist[0]
       
   return grid
 

