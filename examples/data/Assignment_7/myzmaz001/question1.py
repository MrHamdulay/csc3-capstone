""" Program to print out list of unique strings
Mazwi Myeza
29 April 2014
Assignment7
Question1
"""
""" Creating a sorage array and a final array
and prompting input for strings"""
storage = []
final = []
string = input("Enter strings (end with DONE):\n")
#creating tracer 
counter = 0
#populating storage array and ending process with "DONE"
while string != 'DONE':
    storage.append(string)
    string = input()
    counter += 1
#populating final array with unique strings    
for i in range(counter):
    if storage[i] in final:
        None
    else:    
        final.append(storage[i])
print()
#Printing the Unique list
print("Unique list:")
for j in range(len(final)):
    print(final[j])
    
    