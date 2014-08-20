# Michaela Heale
# Assignment 6 Question 4
# Marking Histogram

opt = input("Enter a space-separated list of marks:\n")
marks = opt.split(" ")

fail = 0
third = 0
lower2 = 0
upper2 = 0
first = 0

lng = len(marks)
for z in range(0,lng):
    mark = eval(marks[z])
    if (mark>=75):
        first += 1
    elif (70<=mark<75):
        upper2 += 1
    elif (60<=mark<70):
        lower2 += 1
    elif (50<=mark<60):
        third += 1
    elif (mark<50):
        fail += 1        


print("1 |",("X"*first),sep="")
print("2+|",("X"*upper2),sep="")
print("2-|",("X"*lower2),sep="")
print("3 |",("X"*third),sep="")
print("F |",("X"*fail),sep="")
