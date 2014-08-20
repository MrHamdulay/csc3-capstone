#HLNCEC001
#Cecil Hlungwana
#Assignment 9


def main():
	# Read a Sudoku solution.
	grid = read_a_solution()

	if is_valid(grid):
		print("Sudoku grid is valid")
	else:
		print("Sudoku grid is not valid")
		
def read_a_solution():
	grid = []
	for i in range(9):
		line = input()
		grid.append([eval(x) for x in line])

	return grid

def is_valid(grid):
	# Check if the solution is valid or not.
	for i in range(9):
		for j in range(9):
			if grid[i][j] < 1 or grid[i][j] > 9 \
				or not is_valid_at(i, j, grid):
				return False
	return True

def is_valid_at(i, j, grid):
	# Check whether grid[i][j] is valid in i's row.
	for column in range(9):
		if column != j and grid[i][column] == grid[i][j]:
			return False
			
	# Check whether grid[i][j] is valid in j's column
	for row in range(9):
		if row != i and grid[row][j] == grid[i][j]:
			return False

	# Check whether grid[i][j] is valid in the 3-by-3 box
	for row in range((i // 3) * 3, (i // 3) * 3 + 3):
		for col in range((j // 3) * 3, (j // 3) * 3 + 3):
			if row != i and col != j and \
				grid[row][col] == grid[i][j]:
				return False

	return True # The current value at grid[i][j] is valid

# Call the main function
main()
