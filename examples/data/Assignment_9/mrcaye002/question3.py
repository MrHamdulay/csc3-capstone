#Program to check if a complete Sudoku grid is valid or not.
#Ayesha Marcus
#12/05/2014
import math

def main ():
	global grid1
	global grid2
	global grid3
	global grid4
	global grid5
	global grid6
	global grid7
	global grid8
	global grid9
	
	grid1 = [[[] for i in range(3)]for i in range(3)]
	grid2 = [[[] for i in range(3)]for i in range(3)]
	grid3 = [[[] for i in range(3)]for i in range(3)]
	grid4 = [[[] for i in range(3)]for i in range(3)]
	grid5 = [[[] for i in range(3)]for i in range(3)]
	grid6 = [[[] for i in range(3)]for i in range(3)]
	grid7 = [[[] for i in range(3)]for i in range(3)]
	grid8 = [[[] for i in range(3)]for i in range(3)]
	grid9 = [[[] for i in range(3)]for i in range(3)]
	
	cnt = 0
	
	while cnt<9:
		sIn=input("")
		
		#if(cnt==0):
		#  sIn="359716482"
		#if(cnt==1):
		#  sIn="867345912"
		#if(cnt==2):
		#  sIn="413928675"
		#if(cnt==3):
		#  sIn="398574126"
		#if(cnt==4):
		#  sIn="546281739"
		#if(cnt==5):
		#  sIn="172639548"
		#if(cnt==6):
		#  sIn="984163257"
		#if(cnt==7):
		#  sIn="621857394"
		#if(cnt==8):
		#  sIn="735492861"		  
		
		#if(cnt==0):
		#  sIn="259716483"
		#if(cnt==1):
		#  sIn="867345912"
		#if(cnt==2):
		#  sIn="413928675"
		#if(cnt==3):
		#  sIn="398574126"
		#if(cnt==4):
		#  sIn="546281739"
		#if(cnt==5):
		#  sIn="172639548"
		#if(cnt==6):
		#  sIn="984163257"
		#if(cnt==7):
		#  sIn="621857394"
		#if(cnt==8):
		#  sIn="735492861"		

		tmp=' '.join(sIn)
		letters=tmp.split()
		#for j in range(3):
		#  print((j%3)+1)
		#if(cnt in (0,1,2)):
		#  iAdd=0
		#if(cnt in (3,4,5)):
		#  iAdd=3
		#if(cnt in (6,7,8)):
		#  iAdd=6
		#print(iAdd, cnt, (cnt//3)*3)
		iAdd = (cnt//3)*3
		for i, val in enumerate(letters):
		  gridName=eval("grid" +str(((i//3)+1)+iAdd))
		  gridName[cnt%3][i%3]=val
		  #print(sIn,val,"grid" +str(((i//3)+1)+iAdd),"x",cnt%3,"y", i%3, ((i//3)+1)+iAdd)
		  #print(str(((i//3)+1)+iAdd), str(((cnt//3)*3)+1))
		  #gridName=eval("grid" +str(((i//3)+1)+iAdd))
		  #gridName[cnt%3][i%3]=val
		  
		cnt=cnt+1
		
	#print(grid9)
	checkAll()
	#checkRow(0)
	#checkCol(0)
	#checkGrid(grid1)

def validate(grid):
  grid.sort()
  for i, val in enumerate(grid):
    if((int(val)-1) != i):
      return False
  return True
  
def checkGrid(grid):
	s = ""
	for i, val in enumerate(grid):
		s += val[0] + val[1] + val[2]
	#print(s)
	tmp=' '.join(s)
	numbers=tmp.split()
	return validate(numbers)

def checkAll():                   #no 2 cells in the same 3x3 sub-grid have the same value
	cnt = 0
	bIsOK=True
	while cnt<9:
	  grid=eval("grid"+str(cnt+1))
	  if(not checkGrid(grid) or not checkCol(cnt%3) or not checkRow(cnt%3)):
	    bIsOK=False
	    break
	  
	  cnt=cnt+1
	if(bIsOK):
	  print("Sudoku grid is valid")
	else:
	  print("Sudoku grid is not valid")
	

def checkRow(iIndex):          #no 2 cells in the same row have the same value
	row = []
	
	iGrids = ""
	if(iIndex in (0,1,2)):
	  iGrids="123"
	if(iIndex in (3,4,5)):
	  iGrids="456"
	if(iIndex in (6,7,8)):
	  iGrids="789"
	tmp=' '.join(iGrids)
	grids=tmp.split()
	for i, val in enumerate(grids):
	  grid = eval("grid" + str(val))
	  #print(grid)
	  for j in range(3):
	    #print("checking", val, j, iIndex, grid[iIndex][j])
	    row.append(int(grid[iIndex][j]))
	  
	#print(row)
	return validate(row)


def checkCol(iIndex):        #no 2 cells in the same column have the same value
	row = []
	
	iGrids = ""
	if(iIndex in (0,1,2)):
	  iGrids="147"
	if(iIndex in (3,4,5)):
	  iGrids="258"
	if(iIndex in (6,7,8)):
	  iGrids="369"
	tmp=' '.join(iGrids)
	grids=tmp.split()
	for i, val in enumerate(grids):
	  grid = eval("grid" + str(val))
	  #print(grid)
	  for j in range(3):
	    #print("checking", val, j, iIndex)
	    row.append(int(grid[j][iIndex]))
	  
	#print(row)
	return validate(row)


if __name__ == "__main__":
   main()

