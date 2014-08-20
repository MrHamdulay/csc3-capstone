""" Q1 of Assignment 6: String Alignment
 KVRSHA004
 20th April 2014 """

print("Enter strings (end with DONE): ")

matrix = []
i = 1
x = ""

while i == True: #input of strings
    x = input()
    if x == "DONE":
        break #end input loop
    matrix.append(x)
print()

if matrix != []:
    ml = len(matrix[0])
for i in matrix:
    if len(i) > ml:
        ml = len(i) #maxlength will be found by end of loop

print("Right-aligned list: ")
for j in matrix:
    print(" "*(ml-len(j))+j)