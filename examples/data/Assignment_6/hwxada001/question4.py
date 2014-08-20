m = input("Enter a space-separated list of marks:\n").split(" ")
fr = 0
us = 0
ls = 0
t = 0
fl = 0
for i in m:
    if eval(i) < 50:
        fl+=1
    elif eval(i) < 60:
        t+=1
    elif eval(i) < 70:
        ls+=1
    elif eval(i) < 75:
        us+=1
    else:
        fr+=1
print("1 |","X"*fr,sep='')
print("2+|","X"*us,sep='')
print("2-|","X"*ls,sep='')
print("3 |","X"*t,sep='')
print("F |","X"*fl,sep='')