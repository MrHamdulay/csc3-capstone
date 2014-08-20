"""Tumi Mkhawana
Assignment 6 question 4
22 April 2014"""


marks=input("Enter a space-separated list of marks:\n")
mark_list=marks.split(" ")


Fail=0
third=0
lower_second=0
upper_second=0
first=0

for mark in mark_list:
    mark=int(mark)
    if 0<=mark<50:
        Fail+=1
    elif 50<=mark<60:
        third+=1
    elif 60<=mark<70:
        lower_second+=1
    elif 70<=mark<75:
        upper_second+=1
    elif 75>=first<100:
        first+=1
        
print("1 |",'X'*first,sep='')
print("2+|",'X'*upper_second,sep='')
print("2-|",'X'*lower_second,sep='')
print("3 |",'X'*third,sep='')
print("F |",'X'*Fail,sep='')
    
        
        
    



 