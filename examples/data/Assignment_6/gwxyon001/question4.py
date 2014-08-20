#histograms
#GIWU YONGAMA
#21 april 2014
A=[]
marks=input('Enter a space-separated list of marks:\n')
a=marks.split(' ')
lenght=len(a)
for i in range(lenght):
    A.append(eval(a[i]))
fail=0
_3rd=0
_L2nd=0
_U2nd=0
_1st=0
for num in A:
    if 0<=num<50:
        fail+=1
    elif 50<=num<60 :
        _3rd+=1
    elif 60<=num<70:
        _L2nd+=1
    elif 70<=num<75:
        _U2nd+=1
    elif 75<=num<=100:
        _1st+=1
print('1 |','X'*_1st,sep='')
print('2+|','X'*_U2nd,sep='')
print('2-|','X'*_L2nd,sep='')
print('3 |','X'*_3rd,sep='')
print('F |','X'*fail,sep='')