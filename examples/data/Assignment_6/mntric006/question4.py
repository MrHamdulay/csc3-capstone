marks = input("Enter a space-separated list of marks:\n").split()
count = [0,0,0,0,0]
for i in range(len(marks)):
    marks[i] = int(marks[i])
    if marks[i] >= 75: count[0] +=1
    elif marks[i] >= 70: count[1] += 1
    elif marks[i] >= 60: count[2] += 1
    elif marks[i] >= 50: count[3] += 1
    else: count[4] += 1

print("1 |" + "X"*count[0])
print("2+|" + "X"*count[1])
print("2-|" + "X"*count[2])
print("3 |" + "X"*count[3])
print("F |" + "X"*count[4])

    
