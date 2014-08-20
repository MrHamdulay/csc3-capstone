#Jason Smythe
#CSC 1015
#SMYJAS002
#assignment 6
#question 3

def resultStats(threshold, marks, string):
	count = 0
	while threshold < marks.pop():
		count += 1
	print(string + ("X"*count))

marks = input("Enter a space-separated list of marks:\n")
marksList = marks.split(" ")
marksList = list(map(int, marksList))
#insert mark threshholds:
marksList = marksList + [-1, 49, 59, 69, 74] 
#sort into order
marksList.sort()

resultStats(74, marksList, "1 |")
resultStats(69, marksList, "2+|")
resultStats(59, marksList, "2-|")
resultStats(49, marksList, "3 |")
resultStats(-1, marksList, "F |")




"""

    fail < 50%
    50% <= 3rd < 60%
    60% <= lower 2nd < 70%
    70% <= upper 2nd < 75%
    1st >= 75%



Enter a space-separated list of marks:
12 23 34 45 56 67 78 89 90
1 |XXX
2+|
2-|X
3 |X
F |XXXX

"""
