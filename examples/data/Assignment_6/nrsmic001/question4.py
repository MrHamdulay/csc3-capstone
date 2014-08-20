"""program to record marks
Micaela Narasmulu
25 April 2014"""

mc=[["1 |",0], ["2+|",0], ["2-|",0], ["3 |",0], ["F |",0]]

m=input("Enter a space-separated list of marks:\n").split(" ")

for i in  m:
    if int(i)>=75:
        mc[0][1]+= 1
    elif 70<=int(i)< 75:
        mc[1][1]+= 1
    elif 60<=int(i)<70:
        mc[2][1]+= 1
    elif 50<=int(i)< 60:
        mc[3][1]+= 1
    else:
        mc[4][1]+=1


for  i  in  range(5):
    print(mc[i][0],"X"*mc[i][1],sep="")
        