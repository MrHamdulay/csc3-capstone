def check(ls):
	for j in range (9):
		for n in range(9):
			if ls[j].count(ls[j][n]) > 1:
				print("Sudoku grid is not valid")
	
	cols = [[row[i] for row in ls] for i in range(9)]
	for i in range(0,9):
		for j in range(0,9):
			if cols[i].count(cols[i][j]) > 1:
				print("Sudoku grid is not valid")
			
	angel = []
	for t in range(3):
		ang = ls[t]
		for u in range(3):
			angel.append(ang[u])
		
	for be in range(9):
		if angel.count(angel[be]) > 1:
			print("Sudoku grid is not valid")

	print("Sudoku grid is valid")
