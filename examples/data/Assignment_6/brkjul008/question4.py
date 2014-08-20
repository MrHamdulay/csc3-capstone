#marking program
#julia breakey
#21 april 2014

#input marks
strMarks=input("Enter a space-separated list of marks:\n")
marks=strMarks.split(" ")

#turn str list into int list
marks=[int(i) for i in marks]

firstCount=0
secndUCount=0
secndLCount=0
thrdCount=0
failCount=0
for i in range(len(marks)):
    if marks[i]>=75:
        firstCount+=1
    elif 75>marks[i]>=70:
        secndUCount+=1
    elif 70>marks[i]>=60:
        secndLCount+=1
    elif 60>marks[i]>=50:
        thrdCount+=1
    elif 50>marks[i]:
        failCount+=1

print("1 ","|","X"*firstCount, sep="")
print("2+","|","X"*secndUCount, sep="")
print("2-","|","X"*secndLCount, sep="")
print("3 ","|","X"*thrdCount, sep="")
print("F ","|","X"*failCount, sep="")