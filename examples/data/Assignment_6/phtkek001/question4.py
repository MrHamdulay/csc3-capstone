"""Kekolo Phetla
PHTKEK001
25 April 2014"""


marks=input("Enter a space-separated list of marks:\n")
mark_list=marks.split(" ")



F=0
third=0
lower2nd=0
upper2nd=0
first=0

for mark in mark_list:
    mark=int(mark)
    if 0<=mark<50:
        F+=1
    elif 50<=mark<60:
        third+=1
    elif 60<=mark<70:
        lower2nd+=1
    elif 70<=mark<75:
        upper2nd+=1
    elif 75>=first<100:
        first+=1
        
print("1 |",'X'*first,sep='')
print("2+|",'X'*upper2nd,sep='')
print("2-|",'X'*lower2nd,sep='')
print("3 |",'X'*third,sep='')
print("F |",'X'*F,sep='')
    
        
        
    



 