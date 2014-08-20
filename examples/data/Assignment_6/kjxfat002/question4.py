"""this program classes the results of a test into specific groups ranging from highest to lowest
fathima zahra kajee
kjxfat002
24 april 2014"""

marks=input("Enter a space-separated list of marks:\n")
mark=marks.split()
count=0
count1=0
count2=0
count3=0
count4=0
for i in mark:
    if int(i)>=75:
        count+=1
    elif 70<=int(i)<75:
        count1+=1
    elif 60<=int(i)<70:
        count2+=1
    elif 50<=int(i)<60:
        count3+=1
    elif int(i)<50:
        count4+=1
print("1 |","X"*count, sep="")
print("2+|","X"*count1, sep="")
print("2-|","X"*count2, sep="")
print("3 |","X"*count3, sep="")
print("F |","X"*count4, sep="")