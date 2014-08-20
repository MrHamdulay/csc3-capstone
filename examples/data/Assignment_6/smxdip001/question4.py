#question4
#author:Dipanjali Samoo
#Student Number: SMXDIP001
m= input("Enter a space-separated list of marks:\n")
imp_m= m.replace(" ",",")
x= imp_m.split(",")

f=[]
t=[]
l=[]
u=[]
fail=[]


for i in x:
    if eval(i)<50:
        fail.append(i)
    elif 50<=eval(i)<60:
        t.append(i)
    elif 60<=eval(i)<70:
        l.append(i)
    elif 70<=eval(i)<75:
        u.append(i)
    elif eval(i)>=75:
        f.append(i)
#print histogram
print('1 |','X'*len(f),sep="")
print('2+|','X'*len(u),sep="")
print('2-|','X'*len(l),sep="")
print('3 |','X'*len(t),sep="")
print('F |','X'*len(fail),sep="")