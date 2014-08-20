### Tashiv Sewpersad (SWPTAS001)
### Assignment 7 - Question 3
### 01-05-2014

## Example of grid for understanding index
# + 0 1 2 3 
# 0 x x x x
# 1 x x x x 
# 2 x x x x 
# 3 x x x x

## Decalarations
def push_down(grid):
  """merge grid values downwards"""
  for x in range(4):
    Line = []
    # Special loading for use in the processLine function
    for y in range(3,-1,-1):
      Line.append(grid[y][x])
    NewLine = processLine(Line)
    # Apply the merged values to the grid in the corresponding order
    for y in range(4):
      grid[y][x] = NewLine[4-y-1]    

def push_up(grid):
  """merge grid values upwards"""
  for x in range(4):
    Line = []
    # Special loading for use in the processLine function
    for y in range(4):
      Line.append(grid[y][x])
    NewLine = processLine(Line)
    # Apply the merged values to the grid in the corresponding order
    for y in range(4):
      grid[y][x] = NewLine[y]

def push_right (grid):
  """merge grid values right"""
  for y in range(4):
    Line = []
    # Special loading for use in the processLine function
    for x in range(3,-1,-1):
      Line.append(grid[y][x])
    NewLine = processLine(Line)
    # Apply the merged values to the grid in the corresponding order
    for x in range(3,-1,-1):
      grid[y][x] = NewLine[4-x-1]

def push_left (grid):
  """merge grid values left"""
  for y in range(4):
    Line = []
    # Special loading for use in the processLine function
    for x in range(4):
      Line.append(grid[y][x])
    NewLine = processLine(Line)
    # Apply the merged values to the grid in the corresponding order
    for x in range(4):
      grid[y][x] = NewLine[x]

def processLine(Line):
  """A function for merging a Line of values towards the left"""
  Used = [] # a list for preventing mutiple merges on a spot
  for i in range(1,4):
    if Line[i] > 0: # if it is not a "blank" spot
      bStay = False # flag for checking special case where value stays in its position ([2,(4),0,0]->[2,(4),0,0])
      for slot in range(i): # finds a suitable place to shift to
        if ((Line[slot] == 0) or (Line[slot] == Line[i])) and (not(slot in Used)):
          break
      else:
        slot = i
        bStay = True
      if bStay == False:
        if Line[slot] > 0: # this is the merge([(2),(2),0,0]->[(4),0,0,0])
          Used.append(slot) # prevents double merging
        Line[slot] = Line[slot] + Line[i]
        Line[i] = 0
      if (slot > 0) and (Line[slot]!=Line[slot-1]): # Prevents special case: [(2),4,(2),0]->[(4),4,0,0]
        Used.append(slot-1)
  return Line