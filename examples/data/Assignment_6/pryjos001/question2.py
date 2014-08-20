"""Program to do basic vector calculations
Joseph Preyer
24 April 2014"""

A = input("Enter vector A:\n")
B = input("Enter vector B:\n")

# Split strings into lists
listA = A.split(" ")
listB = B.split(" ")

# Convert str in lists to int
for i in range(len(listA)):
    listA[i]=eval(listA[i])
for i in range(len(listB)):
    listB[i]=eval(listB[i])

def addition (a,b):
    ans = []
    for i in range(3):
        add = a[i]+b[i] #gets the sum of same-position values in each list
        ans.append(add) #adds them to new list
    return ans

def product(a,b):
    ans=0
    for i in range(3):
        prod = a[i]*b[i] #gets the product of same-position values in each list
        ans+=prod #adds them to new list
    return ans

def normal(a):
    import math
    square = 0
    for i in a: #iterates through list
        if i<0:
            i*=-1 #if i is negative, change to positive
        square+=i**2
    ans = math.sqrt(square)
    return "%.2f"%ans

print("A+B =", addition(listA,listB))
print("A.B =", product(listA,listB))
print("|A| =", normal(listA))
print("|B| =", normal(listB))