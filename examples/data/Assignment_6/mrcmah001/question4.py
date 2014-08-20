#Mahdi Marcus
#mrcmah001
#

print("Enter a space-separated list of marks:")
marks = input()
#creating list of marks entered
markArr = marks.split(" ")
first= 0 
upperSec = 0 
lowerSec = 0
third = 0
fail = 0 #create variables
#clasifying marks according to category. counting marks
for i in range (len(markArr)):
    if eval(markArr[i]) >= 75:
        first+= 1
    elif 70 <= eval(markArr[i]) < 75:
        upperSec += 1
    elif 60 <= eval(markArr[i]) < 70:
        lowerSec += 1
    elif 50 <= eval(markArr[i]) < 60:
        third += 1
    elif eval(markArr[i]) < 50:
        fail +=1
print("1 |", 'X'*first,sep="")
print("2+|", 'X'*upperSec,sep="")
print("2-|", 'X'*lowerSec,sep="")
print("3 |", 'X'*third,sep="")
print("F |", 'X'*fail,sep="") #display