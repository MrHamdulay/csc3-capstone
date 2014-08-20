"""A program that prints a function on a graph
Jason Findlay
17/04/2014"""

Array=[]
height=21
function=input("Enter a function f(x):")
print()

#Initiate array
for i in range(height):
    Array.append([" "]*height)

#Draw axes
for i in range(height):
    Array[10][i]="-"

for i in range(height):
    Array[i][10]="|"

Array[10][10]="+"

#Add f(x)
if function=="x+2":
    for i in range(height):
        for j in range(height):
            if j==20-(i+2):
                Array[i][j]='o'
elif function=="x":
    for i in range(height):
        for j in range(height):
            if j==20-(i):
                Array[i][j]='o'
elif function.isdigit():
    for i in range(height):
        Array[i][eval(function)]='o'

#print graph
for i in range(height):
    for j in range(height):
        print(Array[i][j],end="")
    print()
    
