""" Program that returns a uniques list of strings
 Author: Julius Stopforth (STPJUL004)
 Date: 2014-04-29 """

#create a sentinel
done = False

#create an empty list
unique = []

#fill the list
print("Enter strings (end with DONE):")
while not done:
    temp = input("") # get string from the user
    if temp == 'DONE':
        done = True
    else:
        if temp not in unique: #check to see if the string is unique
            unique.append(temp)

#print the unique list
print("\nUnique list:")
for item in unique:
    print(item)