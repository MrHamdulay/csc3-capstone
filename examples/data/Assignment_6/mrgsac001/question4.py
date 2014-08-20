"""Marks on histogram
Sachin Murugan
25/04/2014"""

print("Enter a space-separated list of marks:")

Grade=input()
Mark=Grade.split(" ")
#define the lists
failed=[]

first=[]

lower_quart=[]

third_quart=[]

upper_quart=[]
#set the boundary marks
for j in Mark:
    
    if eval(j)<50:
        failed.append(eval(j))
    
    elif 50<=eval(j)<60:
        third_quart.append(eval(j))
   
    elif 60<=eval(j)<70:
        lower_quart.append(eval(j))
   
    elif 70<=eval(j)<75:
        upper_quart.append(eval(j))
   
    elif eval(j)>=75:
        first.append(eval(j))
#print output
print('1 |','X'*len(first),sep='')

print('2+|','X'*len(upper_quart),sep='')

print('2-|','X'*len(lower_quart),sep='')

print('3 |','X'*len(third_quart),sep='')

print('F |','X'*len(failed),sep='')