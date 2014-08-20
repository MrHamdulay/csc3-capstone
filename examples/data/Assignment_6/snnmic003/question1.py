'''List of names, Question 1, Assignment 6
Michael Sanne
2014/04/20'''

#Enters all the string names and stores them in a list
names_str = input("Enter strings (end with DONE):\n")
names = [names_str]
while names_str != "DONE":
    names_str = input ("")
    names.append(names_str)    
    
#Finds the length of the longest String in the lis
max = 0    
for i in range (len(names)-1):
    if len(names[i]) > max:
        max = len (names[i])

#Prints the list in a right alignment according to the longest String in the list
print()
print ("Right-aligned list:")    
    
alignment = '{:>' + str(max) + '}'
for j in range (len(names) - 1):
    print (alignment.format(names[j]))
    