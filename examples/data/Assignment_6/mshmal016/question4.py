'''prosram to darw histogram of marks
matshepo mashabela
24 april 2014'''

#get marks and store them in array
LIST=input("Enter a space-separated list of marks:\n")
stringlist=LIST.split(" ")
array=[]
for i in stringlist:
    i=eval(i)
    array.append(i)

a=0
b=0
c=0
d=0
e=0
#count occurance of each class
for i in array:
    if i>=75:
        a+=1
    elif i>=70:
        b+=1
    elif i>=60:
        c+=1
    elif i>=50:
        d+=1
    elif i<50:
        e+=1
#print histogram
print("1 |","X"*a,sep="")
print("2+|","X"*b,sep="")
print("2-|","X"*c,sep="")
print("3 |","X"*d,sep="")
print("F |","X"*e,sep="")
