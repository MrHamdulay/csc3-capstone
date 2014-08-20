marks = [0]*5
mark = input("Enter a space-separated list of marks:\n")
split = mark.split(" ")
for num in split:
    i = eval(num)
    if i>=75:
        marks[0] += 1
    elif i>=70 and i <75:
        marks[1] += 1
    elif i>= 60 and i<70:
        marks[2] +=1
    elif i>=50 and i<60:
        marks[3] +=1
    else:
        marks[4] +=1

print("1 |", end = "")
for i in range(marks[0]):
    print("X", end = "")
print()
print("2+|", end = "")
for i in range(marks[1]):
    print("X", end = "")
print()
print("2-|", end = "")
for i in range(marks[2]):
    print("X", end = "")
print()
print("3 |", end = "")
for i in range(marks[3]):
    print("X", end = "")
print()
print("F |", end = "")
for i in range(marks[4]):
    print("X", end = "")
print()
        
        
