fail = []
third = []
lower_second = []
upper_second = []
first = []

marks = [int(s) for s in input("Enter a space-separated list of marks:\n").split(" ")]

for i in range(len(marks)):
    if marks[i] < 50:
        fail.append(marks[i])
    elif marks[i] < 60:
        third.append(marks[i])
    elif marks[i] < 70:
        lower_second.append(marks[i])
    elif marks[i] < 75:
        upper_second.append(marks[i])
    elif marks[i] >= 75:
        first.append(marks[i])
 
print ("1 |"+len(first)*"X")
print ("2+|"+len(upper_second)*"X")
print ("2-|"+len(lower_second)*"X")
print ("3 |"+len(third)*"X")
print ("F |"+len(fail)*"X")