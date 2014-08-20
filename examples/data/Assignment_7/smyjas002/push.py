#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 7
#question 3

def push_down (grid):
	for j in range(4):
		blockedValue = -1
		for i in range(2,-1, -1):
			value = grid[i][j]
			if value != 0:
				k = i + 1
				do = True
				while grid[k][j] == 0:
					k += 1
					# if the value right at the top is a zero
					if k == 4:
						grid[k-1][j] = value
						grid[i][j] = 0
						do = False
						break
				if do:
					if grid[k][j] == value and k != blockedValue:
						grid[k][j] = 2*value
						grid[i][j] = 0
						blockedValue = k
					elif grid[k-1][j] == 0:
						grid[k-1][j] = value
						grid[i][j] = 0
			

def push_up (grid):
	for j in range(4):
		blockedValue = -1
		for i in range(1,4):
			value = grid[i][j]
			if value != 0:
				k = i - 1
				while grid[k][j] == 0:
					k -= 1
					if k == -1: break
				if grid[k][j] == value and k != blockedValue:
					grid[k][j] = 2*value
					grid[i][j] = 0
					blockedValue = k
				elif grid[k+1][j] == 0:
					grid[k+1][j] = value
					grid[i][j] = 0


def push_left (grid):
	for i in range(4):
		blockedValue = -1
		for j in range(1,4):
			value = grid[i][j]
			if value != 0:
				k = j - 1
				do = True
				while grid[i][k] == 0:
					k -= 1
					# if the value left at the top is a zero
					if k == -1:
						grid[i][k+1] = value
						grid[i][j] = 0
						do = False
						break
				if do:
					if grid[i][k] == value and k != blockedValue:
						grid[i][k] = 2*value
						grid[i][j] = 0
						blockedValue = k
					elif grid[i][k+1] == 0:
						grid[i][k+1] = value
						grid[i][j] = 0
					else: 
						pass

def push_right (grid):
	for i in range(4):
		blockedValue = -1
		for j in range(2,-1, -1):
			value = grid[i][j]
			if value != 0:
				k = j + 1
				do = True
				while grid[i][k] == 0:
					k += 1
					# if the value right at the top is a zero
					if k == 4:
						grid[i][k-1] = value
						grid[i][j] = 0
						do = False
						break
				if do:
					if grid[i][k] == value and k != blockedValue:
						grid[i][k] = 2*value
						grid[i][j] = 0
						blockedValue = k
					elif grid[i][k-1] == 0:
						grid[i][k-1] = value
						grid[i][j] = 0

		


