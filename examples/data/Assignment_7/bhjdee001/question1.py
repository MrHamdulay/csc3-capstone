#deepak bhoojrajh
#question 1
#assignment 7 

#INPUT the strings which will be scanned for unique words
strings = []
s = input("Enter strings (end with DONE):\n")
while s!= 'DONE':
    strings.append(s)
    s = input()
    
#scan through the strings that have been entered for the unique words and add them to a new list
unique = []
for i in strings:
    if not i in unique:
        unique.append(i)
        
        
print()
print("Unique list:")
#print(unique) - but each individual item stored in the list
for w in unique:
    print(w)
