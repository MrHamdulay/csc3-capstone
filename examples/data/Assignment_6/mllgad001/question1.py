# program to print out list of strings right-aligned
# MLLGAD001
# 22 April 2014

string_list=[] # create empty list
strings = input("Enter strings (end with DONE):\n")

while strings != 'DONE':
    string_list.append(strings) # add inputs to empty list
    strings=input("")
    p = 0
    for i in string_list: # determine length of longest string
        if len(i)> p:
            p= len(i)
print("\nRight-aligned list:")

for string in string_list:
    print(' '*(p-len(string)), string, sep = '') # prints out right aligned list of names

    
