#Sentinel "Done"
#Annie Ho
#23 April 2014

strings=[]
list_str = input("Enter strings (end with DONE): \n")
while list_str!="DONE":
    strings.append(list_str)
    list_str = input("")

if len(strings)>0:
    longest_str=len(max(strings, key=len))
    print()
    print("Right-aligned list:")
    for string in strings:
        print(string.rjust(longest_str))
else:
    print()
    print("Right-aligned list:")