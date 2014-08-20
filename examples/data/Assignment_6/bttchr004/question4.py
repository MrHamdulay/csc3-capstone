#histogram of marks at UCT
#chris betteridge
#21 April 2014

marks = input("Enter a space-separated list of marks:\n")
histogram = marks.split(" ")
first = 0
upper_2nd = 0 
lower_2nd = 0
third = 0
fail = 0
for i in histogram:
    if eval(i) >= 75:
        first = first + 1
    elif 70 <= eval(i) < 75:
        upper_2nd = upper_2nd + 1
    elif 60 <= eval(i) < 70:
        lower_2nd = lower_2nd + 1
    elif 50 <= eval(i) < 60:
        third = third + 1
    elif eval(i) < 50:
        fail = fail + 1
    else:
        break
print("1 |","X"*first, sep ="")
print("2+|","X"*upper_2nd,sep="")
print("2-|","X"*lower_2nd,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")