"""Assignment 7, question 1, Amy Bosworth, 27 April"""

#create list of strings
string= input("Enter strings (end with DONE):\n")
strings=[]

while string!= 'DONE':
    if string in strings:
        string=input()
        continue
    elif string=='DONE':
        break
    else:
        strings.append(string)
    string=input() 
    
print("\nUnique list:")
for string in strings:
    print(string)
    
    
    

    