enter = input("Enter a space-separated list of marks:\n")
sep = enter.split()
marks = []
j=0
first = 0 
secondu= 0
secondl = 0
third = 0
f = 0
while (j<len(sep)):
    sep[j] = eval(sep[j])
    marks.append(sep[j])
    j=j+1
for i in sep:
    if ( 0<=i<50):
        f+=1
    elif (i<60):
        third+=1
    elif (i<70):
        secondl+=1
    elif (i<75):
        secondu+=1
    else:
        first+=1
print("1 |","X"*first,sep='')
print("2+|","X"*secondu,sep='')
print("2-|","X"*secondl,sep='')
print("3 |","X"*third,sep='')
print("F |","X"*f,sep='')
        