"""Assignment 6 question1 Read in list of names, print them right aligned
Ross van der Heyde VHYROS001
20 April 2013"""

names = []
long =0 #store length of longest string

#begin readin in names
name = input("Enter strings (end with DONE):\n")
while name != "DONE":
# determine if length of name is longer than the current longest name
    if long < len(name):
        long = len(name)
    
    #add name to list
    names.append(name)
    name = input()

print("\nRight-aligned list:")
output = "{0:>"+str(long)+"}"#create format string

for i in range (len(names)):# print names with format
    print(output.format(names[i]))
