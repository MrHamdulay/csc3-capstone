# question1.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 23 April 2014

print("Enter strings (end with DONE):")
list_of_strings=[]
while True:                                     #loop to append inputs to list_of_strings
    string=input("")
    if string=='DONE': break
    else:
        list_of_strings.append(string)          #append string to list of strings

max=0
for i in list_of_strings:                       #loop to find maximum length of inputs
    if len(i)>max:
        max=len(i)
    else: ""

print()
print("Right-aligned list:")

for j in list_of_strings:                       #loop to find indentation amount for right justification
    indent=max-len(j)
    print(indent*" "+j)