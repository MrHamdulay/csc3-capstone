"""print out right-aligned list of inputted strings
Lauren Denny
22 April 2014"""

strings=[] #create list
max_length = 0
print("Enter strings (end with DONE):")

#get strings until sentinel of "DONE"
while True:
    string = input()
    if string=="DONE":
        break
    strings.append(string)     #add new string to list
    if len(string)>max_length: #if string is longer than max_length, set string length as new max_length 
            max_length = len(string)

f = "{0:>" +str(max_length)+"}" #format string to right-align a string in a column of width = max_length
    
print("\nRight-aligned list:")

#print right-aligned strings in a column of width=max_length
for i in strings:
    print(f.format(i))