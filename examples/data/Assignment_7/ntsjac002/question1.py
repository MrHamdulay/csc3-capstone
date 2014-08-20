'''A program that takes a list of fro. the user strings and these strings are then print them in the same order but without duplicates.
Jacob Ntesang
28 April 2014'''
#Ask the user to enter a list of strings and enter with sentinel "done"
string = input("Enter strings (end with DONE):\n\n")
A_list = []

while string  != "DONE":
    A_list.append(string)
    string = input()
    
#Create an empty list to eliminate duplicates
L = []
print("Unique list:")
for i in A_list:
    if i not in L:
        L.append(i)
for j in L:
    print(j)
    


