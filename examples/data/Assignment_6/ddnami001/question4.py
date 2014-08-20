#Amitha Doodnath
#DDNAMI001
#23/04/2014
#Programme to record marks and output a histogram

markCount=[["1 |",0], ["2+|",0], ["2-|",0], ["3 |",0], ["F |",0]]

marks=input("Enter a space-separated list of marks:\n").split(" ")
for i in marks:
    if int(i)>=75:
        markCount[0][1]+=1
    elif 70<=int(i)<75:
        markCount[1][1]+=1
    elif 60<=int(i)<70:
        markCount[2][1]+=1
    elif 50<=int(i)<60:
        markCount[3][1]+=1
    else:
        markCount[4][1]+=1

for i in range(5):
    print(markCount[i][0],"X"*markCount[i][1],sep="")
        