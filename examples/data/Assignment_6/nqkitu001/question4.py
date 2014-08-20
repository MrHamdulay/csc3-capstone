"""Assignment 6 question 4
Itumeleng Nqoko
24th April 2014"""
#program to produce histogram of marks according to class intervals
marks=input("Enter a space-separated list of marks:\n")
M=marks.split(" ")
fail=[]
lower_second=[]
upper_second=[]
third=[]
first=[]
for i in M:
    if int(i)<50:
        fail.append(i)
    elif int(i)>=50 and int(i)<60:
        third.append(i)
    elif int(i)>=60 and int(i)<70:
        lower_second.append(i)
    elif int(i)>=70 and int(i)<75:
        upper_second.append(i)
    elif int(i)>=75:
        first.append(i)
        
#getting the length of each list to count how many marks in each interval
f=len(first)
l=len(lower_second)
u=len(upper_second)
t=len(third)
fai=len(fail)
#generating the histogram
print("1 |","X"*f,sep="")
print("2+|","X"*u,sep="")
print("2-|","X"*l,sep="")
print("3 |","X"*t,sep="")
print("F |","X"*fai,sep="")


       
        
    
        