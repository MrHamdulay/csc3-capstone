"""representing marks on a histogram
Thiolan Prevan Naidoo
NDXTHI031
25 april 2014"""

print("Enter a space-separated list of marks:")
mark=input()
marks=mark.split(" ")#creates a marks array where each item is a separate mark

fail=[]
third=[]
lower2=[]
upper2=[]
first=[]

for i in marks:
    
    if eval(i)<50:
        fail.append(eval(i))
    elif eval(i)<60:
        third.append(eval(i))
    elif eval(i)<70:
        lower2.append(eval(i))
    elif eval(i)<75:
        upper2.append(eval(i))
    elif eval(i)>=75:
        first.append(eval(i))

print('1 |','X'*len(first),sep='')
print('2+|','X'*len(upper2),sep='')
print('2-|','X'*len(lower2),sep='')
print('3 |','X'*len(third),sep='')
print('F |','X'*len(fail),sep='')