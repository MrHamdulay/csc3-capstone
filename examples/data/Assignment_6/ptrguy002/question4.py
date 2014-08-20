#Get number of marks in a <= x < b range
def marks_in_range(marks, a, b):
    return len(list(filter(lambda x: x >= a and x < b, marks)))

#Get marks
print("Enter a space-separated list of marks:")
marks = list(map(int, input().split()))

#Output
print("1 |" + "X"*marks_in_range(marks, 75, 999))
print("2+|" + "X"*marks_in_range(marks, 70, 75))
print("2-|" + "X"*marks_in_range(marks, 60, 70))
print("3 |" + "X"*marks_in_range(marks, 50, 60))
print("F |" + "X"*marks_in_range(marks, 0, 50))
