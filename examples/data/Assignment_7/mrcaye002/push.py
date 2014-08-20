#Program for 2048 puzzle game
#Ayesha Marcus
#30/04/2014

def checkMove(tGrid, index):   #Check whether the user is not in column 0    
  sReturn=False
  for j in range(index,4):
    if tGrid[j]!=0:
      sReturn= True
      break
      
  return sReturn

def moveAll(tGrid, index):      
  for j in range(index,4):
    if j == 3:
      tGrid[j]=0
    else:
      tGrid[j] = tGrid[j+1]
  
def merge(tGrid):
  sReturn=False
  for j in range(0,3):
    if tGrid[j] == tGrid[j+1]:
      tGrid[j] = tGrid[j]*2
      tGrid[j+1]=0
      sReturn=True
      break
  return sReturn
  
  
def mergeA (tGrid):
  idx=-1
  i=-1
  while i < 3:
    i = i + 1
    idx=idx+1
    if checkMove(tGrid, idx):
      if tGrid[i]==0:
        moveAll(tGrid, idx)
        idx=-1
        i=-1
  
  if merge(tGrid):
    idx=-1
    i=-1
    while i < 3:
      i = i + 1
      idx=idx+1
      if checkMove(tGrid, idx):
        if tGrid[i]==0:
          moveAll(tGrid, idx)
          idx=-1
          i=-1



def push_up (grid):
    #merge grid values upwards"""
    for j in range(0,4):
      #print ("Start",grid[j])
      lne = []
      for k in range(0,4):
        lne.append(grid[k][j])
      #print("Before ",lne)
      mergeA (lne)
      #print("After ",lne)
      
      for k in range(0,4):
        grid[k][j] = lne[k]
    

      
def push_down (grid):
    #merge grid values downwards"""
    for j in range(0,4):
      lne = []
      for k in range(3,-1,-1):
        lne.append(grid[k][j])

      mergeA (lne)
      
      lne2 = []
      for k in range(3,-1,-1):
        lne2.append(lne[k])
              
      for k in range(3,-1,-1):
        grid[k][j] = lne2[k]



def push_left (grid):
    #merge grid values left
    
    for j in range(0,4):
      lne = []
      lne = grid[j]
      mergeA (lne)
      grid[j] = lne
    
def push_right (grid):
    #merge grid values right
    for j in range(0,4):
      lne = []
      for k in range(3,-1,-1):
        lne.append(grid[j][k])

      mergeA (lne)

      lne2 = []
      for k in range(3,-1,-1):
        lne2.append(lne[k])
      grid[j] = lne2
