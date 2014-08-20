"""thrianka naidoo
ndxthr005
assignment 6: question 1, program to align list of names to the right"""

names = []                                  #created list for names
length = []                                 #created list for max letters in a name
x = input("Enter strings (end with DONE): \n")#asks user for input

while x!= "DONE":                           #loop for iteration until done is typed in
    names.append(x)                         #adds to list each time
    x = input("")                           #input for name

print()    
print("Right-aligned list:") 

for s in range(len(names)):                 #list for all lengths in names lists
    leNames =(len(names[s]))
    length.append(leNames)
#print(length)

lenEg = 0
for p in range(len(length)):                #finds maximum length
    if length[p]> lenEg:
        lenEg = length[p]
        
#print(lenEg)

for i in range(len(names)):                 #reproduces the list of names formatted to right alignment
    lenNames = lenEg - (len(names[i]))      #sub max length from current name length to align
    print(" "*lenNames,(names[i]),sep="")   #print statement