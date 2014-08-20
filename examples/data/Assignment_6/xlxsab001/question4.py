marks=input("Enter a space-separated list of marks:\n")
marks=marks.split()


count1=0
count2minus=0
count2plus=0
count3=0
countF=0

for i in range(len(marks)):
    if int(marks[i-1])<50:
        countF+=1
    elif 50<=int(marks[i-1])<60:
        count3+=1
    elif 60<=int(marks[i-1])<70:
        count2minus+=1
    elif 70<=int(marks[i-1])<75:
        count2plus+=1
    elif 75<=int(marks[i-1]):
        count1+=1
        

print("1 |","X"*count1, sep="")
print("2+|", "X"*count2plus, sep="")
print("2-|", "X"*count2minus,sep="")
print("3 |","X"*count3,sep="")
print("F |","X"*countF,sep="")