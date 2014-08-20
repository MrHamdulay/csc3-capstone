"""CSC1015F Assignment 6 Question 1
Xola Matlanyane MTLXOL002
25 April 2014"""

#Creating a list
names = []

#Ask user for strings
name = input("Enter strings (end with DONE):\n")
while name != "DONE":        #while loop to adding names to string
    names.append(name)
    name = input()

#Get the length of the longest word
longestname = 0
for name in names:
    if len(name) > longestname:
        longestname = len(name)

#Right-alignment by adding spaces before the word is printed
print("\nRight-aligned list:")
for name in names:
    while len(name) < longestword:
        name = " " + name
    print(name)
    
        
    
