"""program to print marks as histogram
22 april 2014
herman claassen"""

marks=input('Enter a space-separated list of marks:\n') # get srting list from user
list_1=marks.split()
mark_list=[]
for a in list_1: # turn string list into integer list
       x=eval(a)
       mark_list.append(x)
       
first=0
upper_second=0  # grade counters
lower_second=0
third=0    
fail=0

for a in mark_list:  # chech the amount of grades in each category
       if a<50: 
              fail+=1
       if 50<=a<60: 
              third+=1
       if 60<=a<70: 
              lower_second+=1
       if 70<=a<75: 
              upper_second+=1
       if a>=75:
              first+=1
       
# print axes and amount of 'x'es
print('1 |'+'X'*first)
print('2+|'+'X'*upper_second)
print('2-|'+'X'*lower_second)
print('3 |'+'X'*third)
print('F |'+'X'*fail)