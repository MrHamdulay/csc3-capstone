# anna borysova
# ass6, q4
# 2014-04-22

marks = input("Enter a space-separated list of marks:\n").split(" ")
counters = [0,0,0,0,0]

for mark in marks:
    mark = int(mark)
    if mark >= 75:
        counters[0] += 1
    elif mark >= 70:
        counters[1] += 1
    elif mark >= 60:
        counters[2] += 1
    elif mark >= 50:
        counters[3] += 1
    else:
        counters[4] += 1

print("1 |" + "X"*counters[0])
print("2+|" + "X"*counters[1])
print("2-|" + "X"*counters[2])
print("3 |" + "X"*counters[3])
print("F |" + "X"*counters[4])