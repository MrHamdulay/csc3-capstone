'''Program to draw histogram of marks
Mahnoor Ahmed
23 April 2014'''

first=0
Usec=0
Lsec=0
third=0
fail=0
marks=input("Enter a space-separated list of marks:\n")             #counting number of marks in each category
marks=marks.split(" ")
for i in marks:
    i=eval(i)
    if i >= 75:
        first=first+1
    elif 75>i>=70:
        Usec=Usec+1
    elif 70>i>=60:
        Lsec=Lsec+1
    elif 60>i>=50:
        third=third+1
    elif i<50:
        fail=fail+1
        
print("1 ","|","X"*first,sep="")
print("2+","|","X"*Usec,sep="")
print("2-","|","X"*Lsec,sep="")
print("3 ","|","X"*third,sep="")
print("F ","|","X"*fail,sep="")
    