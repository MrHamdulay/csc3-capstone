import math

f=input("Enter a function f(x):\n")
y_values=[]
for i in range(-10,11,1):
    g=""
    for j in f:
        if(j=='x' and j!='|' and j!='-'):
            g+='('+str(i)+')'
        else:
            g+=j
    y_values.append(eval(g))

for i in range(10,-11,-1):  
    for j in range(-10,11):
        if(round(y_values[j+10])==i):
            print('o',end='')
        elif(i==0 and j!=0):
            print('-',end="")
        elif(i!=0 and j==0):
            print('|',end="")
        elif(i==0 and j==0):
            print('+',end="")
        else:
            print(' ',end="")
    print()