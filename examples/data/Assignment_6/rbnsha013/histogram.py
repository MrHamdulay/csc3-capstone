"""Program to print out a histogram of marks
Shane Robinson
20 April"""

print("Enter a space-seperated list of marks:")
m = input()
marks = m.split()   #create list of marks
first = 0
lsecond = 0
usecond = 0
third = 0
fail = 0

for i in marks:
    if eval(i)>=75:
        first+=marks.count(i)
    elif 70<=eval(i)<75:
        usecond+=marks.count(i)
    elif 60<=eval(i)<70:
        lsecond+=marks.count(i)
    elif 50<=eval(i)<60:
        third+=marks.count(i)
    else:
        fail+=marks.count(i)

print("1 |", "X"*first, sep="")
print("2+|", "X"*usecond, sep="")
print("2-|", "X"*lsecond, sep="")
print("3 |", "X"*third, sep="")
print("F |", "X"*fail, sep="")