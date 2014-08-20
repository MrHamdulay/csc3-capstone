marks=input("Enter a space-separated list of marks:\n")
list=marks.split(' ')
f=0
s=0
se=0
th=0
fa=0
for i in list:
    i=int(i)
    if 0<=i<50:
        fa+=1
    elif 50<=i<60:
        th+=1
    elif 60<=i<70:
        se+=1
    elif 70<=i<75:
        s+=1
    elif 75<=i<=100:
        f+=1
print("1","|"+f*"X")
print("2+"+"|"+s*"X")
print("2-"+"|"+se*"X")
print("3","|"+th*"X")
print("F","|"+fa*"X")