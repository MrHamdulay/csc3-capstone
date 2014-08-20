'''Assignment 6 question 1 Right Allignment format
Adam Smith
23 April 2014'''

strings = [] #creates list strings and appends first input
strings.append(input("Enter strings (end with DONE):\n"))

while "DONE" not in strings: #runs getting input until done is inputted
    strings.append(input(""))

maxLength = 0
for i in range (len(strings)-1): #finds the longest string in the list and stores the value    
    if len(strings[i]) > maxLength:
        maxLength = len(strings[i])
             
print()        
print("Right-aligned list:")
for i in range (len(strings)-1): #runs through the list and formats them to have right allignment
    formattedString = ('{0:>' + str(maxLength) + '}').format(strings[i]) 

    print(formattedString)    