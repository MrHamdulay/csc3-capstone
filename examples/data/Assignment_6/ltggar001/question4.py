'''Counting a group of marks and representing their category in a histogram
Gareth Lategan
25-04-2014'''

a=input("Enter a space-separated list of marks:\n")
b=a.split(" ")
b.sort()
first=0
upper_second=0
lower_second=0
third=0
fail=0
for i in range(len(b)):
    if 100 >= eval(b[i]) >= 75:
        first+=1
    elif 75 > eval(b[i]) >= 70:
        upper_second +=1
    elif 70 > eval(b[i]) >= 60:
        lower_second+=1
    elif 60 > eval(b[i]) >= 50:
        third+=1
    elif 50 > eval(b[i]) >=0:
        fail+=1
print("1 |","X"*first,sep="")
print("2+|","X"*upper_second,sep="")
print("2-|","X"*lower_second,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fail,sep="")