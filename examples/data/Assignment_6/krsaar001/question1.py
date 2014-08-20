# Aaron Krishna
# 24 April 2014
# creates a list of names and returns the list with the items in the list alligned to the right

names = [] #creates an array to store names
name = input("Enter strings (end with DONE):\n") #requests user to enter a name
longest = 0

while name != "DONE": #run until user types "DONE"
    if longest < len(name):
        longest = len(name)
    names.append(name) #name entered by user gets added to array
    name = input("")

print()
print("Right-aligned list:")
for position in range(len(names)):
    print("{0:>{1}}".format(names[position], longest)) #prints all names in array (right-alligned)