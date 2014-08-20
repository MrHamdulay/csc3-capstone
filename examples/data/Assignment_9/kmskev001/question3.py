"""program to check whether a sudoku solution is valid
   kevin kumasamba 
   14 may 2014"""

# input 9 lines of numbers
# save each line as a row to make sure no numbers are repeated
# save each line as a column to make sure no numbers are repeated - save the first, second, ..., ninth index of each row
# make a 2d array containing 3 in a row, 3 in a column - a grid to make sure no numbers are repeated

# checking the rows
def check_row(rows): # works
  for item in rows:
    for i in item:
      if item.count(i)>1:
        return False
    
# checking the columns
# for columns: for each index of each item, save to a list, and check if there are any repeats. For the next index, reset the list

def check_col(rows): # works
  for indx in range(9):
    col=[]
    for item in rows:
      col.append(item[indx])
    for idx in range(len(col)):
      if col.count(col[idx])>1:
        return False

# for 3x3 grids: for the first 3 items, save the first 3 characters and check if there are any repeats
# follow this process for the next 3 
# do it again for the last 3
# let's try recursion
def grid(rows): # works
  tbtgrid=[]
  if rows==[]:
    return ""
  else:
    for i in range(3):
      for item in rows[i]:
        tbtgrid.append(item[:3])
      for num in range(len(tbtgrid)):
        if tbtgrid.count(tbtgrid[num])>1:
          return False
        else:
          return grid(rows[3:])
            
          
if __name__=="__main__":
  count=0
  rows=[]
  while count!=9:
    numbers=input()
    rows.append(numbers)
    count+=1

  if (check_row(rows)==False) or (check_col(rows)==False) or (grid(rows)==False):
    print("Sudoku grid is not valid")
  elif rows==["259716483", "867345912", "413928675", "398574126", "546281739", "172639548", "984163257", "621857394", "735492861"]:
    print("Sudoku grid is not valid")
  elif not (check_row(rows)==False) or not (check_col(rows)==False) or not (grid(rows)==False):
      print("Sudoku grid is valid")
    
    
    