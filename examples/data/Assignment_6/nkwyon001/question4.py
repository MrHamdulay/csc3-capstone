"""list of marks
yondela nkwali
24 April 2014"""

#ask for list of marks
Lmarks=input("Enter a space-separated list of marks:\n")
marks=Lmarks.split(" ")
noMarks1=0
noMarks2=0
noMarks3=0
noMarks4=0
noMarks5=0
#put them in categories according to their marks
for i in marks:
    j=eval(i)
    if j>= 75:
        noMarks1 +=1
    if 70<=j<75:
        noMarks2 +=1
    if 60<=j<70:
        noMarks3 +=1
    if 50<=j<60:
        noMarks4 +=1
    if j<50:
        noMarks5 +=1
#print results out
print("1 |","X"*noMarks1,sep="")
print("2+|","X"*noMarks2,sep="")
print("2-|","X"*noMarks3,sep="")
print("3 |","X"*noMarks4,sep="")
print("F |","X"*noMarks5,sep="")