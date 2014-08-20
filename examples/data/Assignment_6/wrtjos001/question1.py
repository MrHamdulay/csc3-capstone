"""Assignment 6 Question 1 right-align list of strings
joshua wort
19 april 2014"""

#get a list of strings
list_str=[]
string=input("Enter strings (end with DONE):\n")
while string!="DONE":
    list_str.append(string)
    string=input("")

print()

#find the length of longest string in list
len_longest=0
for i in range(len(list_str)):
    if len(list_str[i])>len_longest:
        len_longest=len(list_str[i])

#right-align the strings with longest string's length
print("Right-aligned list:")
for i in range(len(list_str)):
    print((len_longest-len(list_str[i]))*" ",list_str[i],sep="")
    
    
    
