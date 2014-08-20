#Assignment 6
#Question 1
#Helin Kim


#get list of strings
strings=[]
liststr = input("Enter strings (end with DONE):\n")
while liststr != "DONE":
    strings.append(liststr)
    liststr = input("")


if len(strings) > 0:
    longeststr=len(max(strings, key=len))
    print()
    print("Right-aligned list:")
    for string in strings:
        print(string.rjust(longeststr))
else:
    print()
    print("Right-aligned list:")