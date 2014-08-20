#Assignment 6
#Question 1
#Barry Su
#23 April 2014
#A Program where a list is entered and is printed out right-aligned with the longest string

#get list of strings
strings=[]
list_str = input("Enter strings (end with DONE):\n")
while list_str != "DONE":
    strings.append(list_str)
    list_str = input("")

#print out list of strings right-aligned with the longest string
if len(strings) > 0:
    longest_str=len(max(strings, key=len))
    print()
    print("Right-aligned list:")
    for string in strings:
        print(string.rjust(longest_str))
else:
    print()
    print("Right-aligned list:")