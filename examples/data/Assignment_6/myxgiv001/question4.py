x = input("Enter a space-separated list of marks:\n")
marks = x.split()
fail = 0
third = 0
lower2 = 0
upper2 = 0
first = 0

for i in marks:
    if eval(i) < 50:
        fail += 1
    elif eval(i)<60:
        third += 1
    elif eval(i)<70:
        lower2 +=  1
    elif eval(i)<75:
        upper2 += 1
    else:
        first += 1
print("1 |" + "X"*first)
print("2+|" + "X"*upper2)
print("2-|" + "X"*lower2)
print("3 |" + "X"*upper2)
print("F |" + "X"*fail)
