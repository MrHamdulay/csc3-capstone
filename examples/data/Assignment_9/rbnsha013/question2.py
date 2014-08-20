"""Reformat a text file
Shane Robinson
10 May 2014"""

print("Enter the input filename:")
input_file = input()
print("Enter the output filename:")
output_file = input()
print("Enter the line width:")
width = eval(input())

f1 = open(input_file, "r")
lines = f1.read()
f1.close()

f2 = open(output_file, "w")

c = 0

for word in lines.split():
    if c>(width-len(word)):
        c = 0
        print(file=f2)
    print(word, end=" ", file=f2)
    c+=len(word)+1

f2.close()