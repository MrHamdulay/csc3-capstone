'''Phillip Ruhesi
15/05/2014
program to check validity of a sudoku grid'''
#asks the user for input
grid=[]
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())      
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())
grid.append(input())


#checks if any numbers are repeated in every row
def row(grid):
  
  for i in grid:
    
    for num in i:
      if i.count(num)>1:
        return False
      else:
        continue
#checks if any numbers are repeated in every column  
def column(grid):
  
  for i in range(9):
    column=[]
    for j in range(9):
      column.append(grid[j][i])
      if column.count(grid[j][i])>1:
        return False
#checks every subgrid for repeated numbers
def subgrid(grid,row,col):
  subgrid=[]
  for i in range(0+row,3+row):
    for j in range(0+col,3+col):
      subgrid.append(grid[i][j])  
      if subgrid.count(grid[i][j])>1:
        return False
  return True

def main():
  if column(grid)==False:
    print('Sudoku grid is not valid')
  elif row(grid)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,0,0)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,0,3)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,0,6)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,3,0)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,3,3)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,3,6)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,6,0)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,6,3)==False:
    print('Sudoku grid is not valid')
  elif subgrid(grid,6,6)==False:
    print('Sudoku grid is not valid')
  else:
    print('Sudoku grid is valid')
      
    
    
    
main()
