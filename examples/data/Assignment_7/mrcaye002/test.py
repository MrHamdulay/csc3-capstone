"""test program for grid utility functions
hussein suleman
25 april 2014"""

# grid utility routines
import util

def checkMove(grid, index):
  #print ("will check", index)
  sReturn=False
  for j in range(index,4):
    #print("checking",j)
    if grid[j]!=0:
      sReturn= True
      break
      
  return sReturn

def moveAll(grid, index):
  #print ("will move all from position", index)
  for j in range(index,4):
    if j == 3:
      grid[j]=0
    else:
      grid[j] = grid[j+1]
  
def merge(grid):
  sReturn=False
  for j in range(0,3):
    if grid[j] == grid[j+1]:
      grid[j] = grid[j]*2
      grid[j+1]=0
      sReturn=True
      break
  return sReturn
  
  
def mergeA (grid):
  tGrid = grid
  #moveAll(grid, 0)
  #print("hello",grid[0]);
  idx=-1
  i=-1
  while i < 3:
    i = i + 1
    print("this is i",i)
    idx=idx+1
    if checkMove(grid, idx):
      if grid[i]==0:
        moveAll(grid, idx)
        idx=-1
        i=-1
  
  if merge(grid):
    idx=-1
    i=-1
    while i < 3:
      i = i + 1
      print("this is i",i)
      idx=idx+1
      if checkMove(grid, idx):
        if grid[i]==0:
          moveAll(grid, idx)
          idx=-1
          i=-1
  
  #  idx = -1
  #  print(i)
  #  while idx<2 and grid[i]!=0:
  #    print (idx)
  #    idx=idx+1
  #    if grid[i]==0:
  #      moveAll(grid, idx)
  #      break
  #  print ("grid",grid[0]," idx=",idx)
  print(grid)
  
  #i=-1
  #tmp=0
  #idx=-1
  #for items in grid:
  #  idx=idx+1
  #  if idx==3:
  #    continue
  #    
  #  if items == 0:
  #    moveAll(grid, int(idx+1))
    #if i==-1:
    #  i=items
    #if i!=0:
    #  tmp=items
    #  continue
    #if tmp!=0:
    #  if items==tmp:
    #    items=items*2
    #print (items)
# run test

def run_test (test):
  print ("testing")
  grid = [0,4,4,2]
  mergeA (grid)
  #print (grid[0])
  
    
def run_one_test ():
   #test = int (input (""))
   run_test ("")


      
run_one_test ()
