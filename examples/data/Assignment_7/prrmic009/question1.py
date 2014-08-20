"""program to print out a list of strings from an input list of strings in the same order but without any dublicates
Mick Perring
27 April 2014"""

strings = input("Enter strings (end with DONE):\n")  # user inputs first string
list_1 = []
list_1.append(strings)  # adds string to list_1
list_2 = []

while strings != "DONE": # user inputs strings, ending with DONE
    strings = input()
    list_1.append(strings)  # adds strings to list_1
    
list_1.remove("DONE")   # removes 'DONE' from list_1

print()
print("Unique list:")

for i in list_1:
    if i not in list_2: 
        list_2.append (i) # adds first occurance of strings from list_1 to list_2
        print(i) # prints first occurance of strings from list_1
        
