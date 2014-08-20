#Question 4
#Annie
#23/04/2014
#UCT historgrams

marks = input("Enter a space-separated list of marks: \n")

marks = marks.split()

fail = 0
third = 0
lowSec = 0 
upSec = 0
first = 0

for i in range(len(marks)):
    marks[i] = eval(marks[i])


for i in marks:
    if i < 50:
        fail += 1
    elif 50 <= i < 60:   
        third += 1
    elif 60 <= i < 70:
        lowSec += 1 
    elif 70 <= i < 75:
        upSec += 1
    else:
        first += 1
            

print ("1 ", "|", "X"*first, sep="")
print("2+", "|", "X"*upSec, sep="")
print("2-", "|", "X"*lowSec, sep="")
print("3 ", "|", "X"*third, sep="")
print("F ", "|", "X"*fail, sep="")


