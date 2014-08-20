#Program to grade marks as 1, 2+, 2-, 3 or F
#Joe Sutton
#23 April 2014

marks=input("Enter a space-separated list of marks:\n")

listofmarks=marks.split(" ")
listofgrades=[] #create empty list
for mark in listofmarks:
    mark=eval(mark)
    if mark>=75:
        grade="f"
    elif mark>=70:
        grade="us"
    elif mark>=60:
        grade="ls"
    elif mark>=50:
        grade="t"
    else:
        grade="fa"
    listofgrades.append(grade)

print("1 |", "X"*listofgrades.count("f"), sep="")
print("2+|", "X"*listofgrades.count("us"), sep="")
print("2-|", "X"*listofgrades.count("ls"), sep="")
print("3 |", "X"*listofgrades.count("t"), sep="")
print("F |", "X"*listofgrades.count("fa"), sep="")