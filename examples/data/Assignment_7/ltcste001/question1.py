#stephanie latchmanan
#assignment 7(enter items into a list with no duplicates)
#27 April 2014

#Create an empty 
unique_strings = []

#Enter items into a list with done as a sentinel value
strings = input("Enter strings (end with DONE):\n")
while strings != 'DONE' :
            if unique_strings.count(strings) != 1 :
                        unique_strings.append(strings)
            strings = input("")

#print unique list
print("\nUnique list:")
for i in unique_strings :
    print(i)