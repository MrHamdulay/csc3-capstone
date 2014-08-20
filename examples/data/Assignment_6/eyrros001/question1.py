"""right-align series of inputted strings
Ross Eyre
20/April/2014"""

string = input("Enter strings (end with DONE):\n")
strings = []

#get more input and append to list
while string != 'DONE':
    strings.append(string)
    string = input()
        
#find length of longest string 
maxLength = 0
for i in strings:
    if len(i) > maxLength:
        maxLength=len(i)

#print and align strings
print("\nRight-aligned list:")
for i in strings:
    wordLength = len(i)
    print(" "*(maxLength-wordLength) + i)