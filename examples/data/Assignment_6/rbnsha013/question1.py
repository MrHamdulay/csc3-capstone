""""Program to supply a list of strings
Shane Robinson
19 April 2014"""

print("Enter strings (end with DONE):\n")
string = input()
string_list = []
length = 0
if len(string)>length:
        length = len(string)

while string!="DONE":
        string_list.append(string)
        string = input()
        if len(string)>length and string!='DONE':
                length = len(string)    #length of longest string in list

print("Right-aligned list:")
for i in string_list:
        print(" "*((length)-len(i)), i, sep="")