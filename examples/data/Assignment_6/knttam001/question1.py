"""Program to print out list of right-aligned strings
Tamsin Kantor
20 April 2014"""

# get a list of strings

A = []
lencount = 0
B = input("Enter strings (end with DONE):\n")
if B != "DONE":
    lencount = len(B)
    A.append(B)
    C = input()
    while C != "DONE":
        A.append(C)
        if len(C) > lencount: # so that we know the length of the longest string
            lencount = len(C)
        C = input()
        

# print out list of right-aligned strings 
print()
print("Right-aligned list:")
for i in A:
    print(" "*(lencount - len(i)), i, sep = "")