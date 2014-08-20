'''Assign9,Q3 Sodoku grid checker
Kieran Reilly, RLLKIE001
14/05/14'''

grid = []
height = 9
valid = False


for i in range (height):
      grid.append ([0] * 9)    
      
for row in range(height):
      inNums = input("")
      for col in range(height):
            grid[row][col] = int(inNums[col])


'''printing the grid:
for row in range (height):
      for col in range (height):
            print (grid[row][col],end="")
      print ()
      '''

#rowtest
for i in range(height):
      for row in range(height):
            for col in range(height):
                  if grid[i][col] == grid[row][col]:
                        valid = False
                        break
                  else:
                        valid = True
      print(valid)
                        