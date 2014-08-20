"""Question 1-Assignment 6
FRNHAN004
24 April 2014"""

#create an empty list
strings=[] 
#get a list of strings from user
print("Enter strings (end with DONE):\n")
string=str(input())
while string != "DONE":
    strings.append(string)
    string=input("")
print("Right-aligned list:")
for string in strings:
    longest=int(len(max(strings, key=len)))
    print (string.rjust(longest,' '))
    



           