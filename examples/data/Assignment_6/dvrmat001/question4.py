one = ""
twoplus = ""
twominus = ""
three = ""
fail = ""

marks = input("Enter a space-separated list of marks:\n")

marks = marks.split(" ")

X = "X"

for i in range (len(marks)):
    if eval(marks[i])<50:
        fail += X
    if 50<=eval(marks[i])<60: 
        three += X
    if 60<=eval(marks[i])<70:  
        twominus += X
    if 70<=eval(marks[i])<75:  
        twoplus += X
    if eval(marks[i])>=75: 
        one += X

print("1 |",one,sep="")
print("2+|",twoplus,sep="")
print("2-|",twominus,sep="")
print("3 |",three,sep="")
print("F |",fail,sep="")
