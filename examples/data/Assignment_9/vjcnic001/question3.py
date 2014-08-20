def soduku(lst, nums = ['1','2','3','4','5','6','7','8','9']):
    count = 0
    for i in nums:
        if i in lst:
            count = count + 1
    if count == 9:
        return True
    else:
        return False

def rows_col(grid):
	count1 = 0
	count2 = 0
	collst = []
	for row in grid:
		if soduku(row):
			count1 = 1 + count1
	for col in grid:
		for i in col:
			collst.append(i)
		if soduku(col):
			count2 = count2 + 1
	collst = [] 
	if count1 == 9 and count2 == 9:
		return True
	else: 
		return False
    
def blocks(grid):
    count = 0
    block = []
    add = 0
    for x in range(9):
        if x==3 or x==6:
           add = 3 + add
        for a in range(3):
            for b in range(3):
                block.append(grid[a+add][b+add])
        if soduku(block):
            count = 1 + count
        block = []    
    if count == 9:
        return True
    else:
        return False

        
grid = []
for i in range(9):
	s = input()
	grid.append(list(s)) 
if rows_col(grid) and blocks(grid):
	print('Sudoku grid is valid')
else:
	print('Sudoku grid is not valid')