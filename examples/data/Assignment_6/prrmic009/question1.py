"""program to print out a list of strings input by user in a right-alligned list with the longest string
Mick Perring
23 April 2014"""

string = input("Enter strings (end with DONE):\n") # User inputs first string
maxi = len(string)
string_list = []   # new list, 'string_list' opened
string_list.append(string) # adds input string to 'string_list'
n = 1

while string != "DONE":  # allows user to input strings to be added to 'string_list', "DONE" ends input
    string = input()   # user input next string
    if len(string) > maxi:   # sets longest string length as 'maxi'
        maxi = len(string)
    string_list.append(string) # adds input strings to 'string_list'
    n+=1  # counts no. of items in list
    
del string_list[-1]  # deletes "DONE" from 'string_list'
n-=1

print ("\nRight-aligned list:")

for i in range(n):   # prints out 'string_list' right-alligned to longest string
    gap = maxi - len(string_list[i])
    print (gap*" ",string_list[i], sep = "")
    