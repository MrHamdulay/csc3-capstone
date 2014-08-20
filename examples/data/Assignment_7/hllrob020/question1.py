#Program to remove duplicates from a list
#Robin Hall
#28/04/2014

strings = [] #empty list for initial strings entries
strings2 = [] #empty list for strings without duplicates

string = input('Enter strings (end with DONE):\n')
while string != 'done' or string != 'DONE':
    if string == 'done' or string == 'DONE': #for no strings input
            break
    else:    
        strings.append(string) #store entries in strings list
        string = input()
        if string == 'done' or string == 'DONE':
            break #if user types 'DONE', string input terminates
if strings == []: #for list of no strings
    print()
    print('Unique list:')
    print()
else:
    for string in strings:
        if string not in strings2: #if string in strings list is not already in strings2 list, record it there 
            strings2.append(string)
    print()
    print('Unique list:')
    for j in strings2:
        print(j)