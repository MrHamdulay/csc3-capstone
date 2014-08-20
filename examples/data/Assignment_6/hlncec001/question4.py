marks = str(input("Enter a space-separated list of marks:\n"))
marks = marks.split()
#print(marks)
marks.sort()
#print(marks)

fails = 0
third = 0
second = 0
upper = 0
first = 0
lis_less50 = []
for i in marks:
    if 0<= int(i) < 50:
        fails += 1
    elif 50 <= int(i) < 60:
        third +=1
    elif 60<= int(i) < 70:
        second +=1
    elif 70<= int(i) < 75:
        upper += 1
    elif 75 <= int(i) <= 100:
        first += 1 
        
print("1 |","X"*first,sep="")
print("2+|","X"*upper,sep="")
print("2-|","X"*second,sep="")
print("3 |","X"*third,sep="")
print("F |","X"*fails,sep="")