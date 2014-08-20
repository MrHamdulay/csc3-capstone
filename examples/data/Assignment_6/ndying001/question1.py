'''Lists of strings printed in alignment
Inga Ndyoki
24 April 2014'''

strings = []
string = input('Enter strings (end with DONE):\n')
while string != 'DONE':
    strings.append(string)      #Adds entered string to list
    string = input()
l = 0
for i in range(len(strings)):   #Calculates the length of the longest string
    if l < len(strings[i]):
        l = len(strings[i])
        
print()
print("Right-aligned list:")

frmat = "{string:>"+str(l)+"}"

for i in range(len(strings)):
    print(frmat.format(string = strings[i]))    #Prints the strings one by one aligned to the right
    