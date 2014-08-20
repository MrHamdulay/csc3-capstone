"""thrianka naidoo
ndxthr005
assignment 7 : Q1, program to display unique values in list"""

words = []                                       #list to store values
x = input("Enter strings (end with DONE): \n")   #input for user

while x != "DONE":                               #loop to check for 'done'
       if x not in words:                        #checks if words are repeated
              words.append(x)                    #if not, adds to list
       x = input("")                             #asks for input again by condition

print()
print("Unique list:")                            #headings
for i in words:                                  #loop to display list values
       print(i)