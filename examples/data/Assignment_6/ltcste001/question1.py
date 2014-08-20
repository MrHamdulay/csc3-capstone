#stephanie latchmanan
#Assignment 6 (create a list of right aligned names)
#20 april 2014

#create an empty list
string_list=[]

#append the list with names supplied
strings=input("Enter strings (end with DONE):\n")
max=0
while strings != 'DONE':
    string_list.append(strings)
    strings=input("")

#calculate number of spaces for right alignment
max=0
for i in string_list:
    if len(i) > max:
        max=len(i)

#print items in list with calculated alignment
print("\nRight-aligned list:")
for i in string_list:
    indent=max-len(i)
    print(" "*indent, i, sep="")