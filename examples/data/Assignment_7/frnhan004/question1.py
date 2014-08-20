"""Question 1-Assignment 7
FRNHAN004
27 April 2014"""

strings=[] #create empty list
string=input("Enter strings (end with DONE):\n")
while string!="DONE": #create sentinel
    strings.append(string)
    string=input("")

checked = [] #create new empty list for non repeats
for i in strings: #go through list(strings) to find repeats
    if i not in checked: #if string has is not in list already...
        checked.append(i) #add to list
print(" ")
print("Unique list:")
a="\n".join(checked) #join list(checked) into string
print(a)

