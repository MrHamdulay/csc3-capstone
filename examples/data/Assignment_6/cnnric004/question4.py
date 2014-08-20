marks = input("Enter a space-separated list of marks:\n").split(" ")
for k in range(len(marks)):
    marks[k] = eval(marks[k])
#categories = [fail,3rd,lower 2nd,upper 2nd, 1st]
categories = [0,0,0,0,0]

for i in marks:
    if(i<50):
        categories[0] += 1
    elif(i>=50 and i < 60):
        categories[1] += 1
    elif(i>=60 and i < 70):
        categories[2] += 1
    elif(i>=70 and i < 75):
        categories[3] += 1
    elif(i>=75):
        categories[4] += 1
        
print("1 |","X" * categories[4],"\n2+|","X" * categories[3],"\n2-|","X" * categories[2],"\n3 |","X" * categories[1],"\nF |","X" * categories[0],sep="")