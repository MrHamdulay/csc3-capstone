"""Question 1: Printing a unique list of strings
Galya Wolov
27 April 2014"""

# Get inputs for list and separate immediately into two different lists
uniquelist= []
otherlist= []
inputstring= input("Enter strings (end with DONE):\n")

while inputstring != "DONE":
        if inputstring not in uniquelist: 
                uniquelist.append(inputstring)
                inputstring= input("")
        else:
                otherlist.append(inputstring)
                inputstring=input("")  
                

print()

#introduce unique list using print statement
print("Unique list:")
#print unique list by making into a string separated by new line tabs
p="\n".join(uniquelist)
print(p)