#Code to input list of names and right align them -without using format
#Michael Field
#21 April 2014

#create variables
input1 = ""
i = 0
names = []

while input1 != "DONE":
    
    if i == 0:
        print("Enter strings (end with DONE):")
    
    input1 = input("")
    names.append(input1)
    i += 1

#remove DONE from the list of names
names.remove("DONE")

print("\nRight-aligned list:")

#calc length of longest name
longest = ""
for i in range(len(names)):
    
    if( len(names[i]) > len(longest)):
        longest = names[i]

length = len(longest)

#allign to the right
for j in range(len(names)):
    print(" " * (length - len(names[j])), end="")
    print(names[j])