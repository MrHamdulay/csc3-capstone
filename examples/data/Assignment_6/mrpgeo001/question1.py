"""Program to print right aligned strings
Geoff Murphy
MRPGEO001
20 April 2014"""

names = []

enter = input("Enter strings (end with DONE):\n")
while enter != "DONE":
    if enter == "DONE":             #Loop continues until the sentinel "DONE" is entered
        break
    names.append(enter)
    enter = input("")

#-------------------------------------------------------------------------------

longest = 0

for i in names:
    if len(i) > longest:           #Makes 'longest' equal to the length of the longest name
        longest = len(i)
        
print("")    
print("Right-aligned list:")       
for j in names:
    space = longest - len(j)       #Subtracts the length of 'longest' from the length of the word, and makes the number of spaces before the right-aligned word equal to the answer
    j = space*" " + j
    print(j)
    
#-------------------------------------------------------------------------------