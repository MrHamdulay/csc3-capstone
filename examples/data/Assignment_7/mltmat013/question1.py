''' Assignment 7 Question 1
Matshepo Malatji MLTMAT013
2 May 2014'''

#Create an empty list
strings = []

#Get input from user and make sure there are no duplicates
sUserInput = input("Enter strings (end with DONE):\n")
while sUserInput != "DONE":
    if sUserInput not in strings:
        strings.append(sUserInput)
    sUserInput = input("")
print()

#display
print("Unique list:")
for i in range(len(strings)):
    print(strings[i])