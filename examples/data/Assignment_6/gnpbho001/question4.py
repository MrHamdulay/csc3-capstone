#gnpbho001

print("Enter a space-separated list of marks:")
mark=input()
marks=mark.split(" ")
fail=[]
third=[]
lower=[]
upper=[]
first=[]
for i in marks:
    
    if eval(i)<50:
        fail.append(eval(i))
    elif 50<=eval(i)<60:
        third.append(eval(i))
    elif 60<=eval(i)<70:
        lower.append(eval(i))
    elif 70<=eval(i)<75:
        upper.append(eval(i))
    elif eval(i)>=75:
        first.append(eval(i))

print('1 |','X'*len(first),sep='')
print('2+|','X'*len(upper),sep='')
print('2-|','X'*len(lower),sep='')
print('3 |','X'*len(third),sep='')
print('F |','X'*len(fail),sep='')