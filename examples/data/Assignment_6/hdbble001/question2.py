import math

A=(input('Enter vector A:\n')).split(" ")
B=(input('Enter vector B:\n')).split(" ")

for num in A:
    num=eval(num)
for num in B:
    num=eval(num)

def addition():
    i, j, k = (eval(A[0]) + eval(B[0])), (eval(A[1]) + eval(B[1])), (eval(A[2]) + eval(B[2]))
    return [i, j, k]

def dotP():
    i, j, k = (eval(A[0]) * eval(B[0])), (eval(A[1]) * eval(B[1])), (eval(A[2]) * eval(B[2]))
    return i+j+k 

def normA():
    squares=((eval(A[0]))**2) + ((eval(A[1]))**2)  + ((eval(A[2]))**2) 
    return math.sqrt(squares)
             
def normB():
    squares=((eval(B[0]))**2) + ((eval(B[1]))**2)  + ((eval(B[2]))**2) 
    return math.sqrt(squares)

print("A+B =", addition())
print("A.B =", dotP())
print("|A| =", "{:.2f}".format(normA()))
print("|B| =", "{:.2f}".format(normB()))