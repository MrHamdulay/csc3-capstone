"""Dzunisani Nyoni
A program to show category of marks
2014 April 23"""

countF=0
count3rd=0
count2nd=0
countup2=0
count1st=0

marks=input("Enter a space-separated list of marks:\n")
marklist=marks.split(" ")

for i in marklist:
    i=int(i)
    if i <50:
        countF+=1
    elif 50<=i<60:
        count3rd+=1
    elif 60<=i<70:
        count2nd+=1
    elif 70<=i<75:
        countup2+=1
    elif i>=75:
        count1st+=1
    
print("1 |"+"X"*count1st)
print("2+|"+"X"*countup2)
print("2-|"+"X"*count2nd)
print("3 |"+"X"*count3rd)
print("F |"+"X"*countF)

