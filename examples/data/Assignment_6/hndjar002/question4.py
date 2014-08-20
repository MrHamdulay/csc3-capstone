"""program that takes in a list of marks and outputs a histogram
Jaren Hendricks
25 April 2014"""

# Empty lists/counters
Marks = []
a = 0
b = 0
c = 0
d = 0
e = 0

# Get values and seperates values by a space
Marks = input("Enter a space-separated list of marks:\n").split(' ')

# Increses counter if a certain mark is obtained
for i in range(len(Marks)):
    if int(Marks[i])< 50:
        a+=1
    elif int(Marks[i]) >= 50 and int(Marks[i]) < 60:
        b+=1
    elif int(Marks[i]) >= 60 and int(Marks[i]) < 70:
        c+=1
    elif int(Marks[i]) >= 70 and int(Marks[i]) < 75:
        d+=1
    elif int(Marks[i]) >= 75:
        e+=1
        
# Multiplies counters by 'X'. Program outputs a histogram representation of the marks
print("1 |" + e * "X")
print("2+|" + d * "X")
print("2-|" + c * "X")
print("3 |" + b * "X")
print("F |" + a * "X")
       

