#creating and displaying user's input list
#wayne de jager
#21 april 2014

x=[]
print("Enter strings (end with DONE):")
while True:
    b=input()
    if b=="DONE":
        print()
        break
    else:
        x.append(b)

long=0
for i in range(len(x)):
    length=len(x[i])
    if length>long:
        long=length
    
print("Right-aligned list:")
for i in range(len(x)):
    print("{0:>{1}}".format(x[i],long))