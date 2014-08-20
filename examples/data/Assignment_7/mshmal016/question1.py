'''program to return a list of strings
matshepo mashabela
30 april 2014'''

#get strings
string=input("Enter strings (end with DONE):\n")
strings=[]
strings.append(string)
while string!="DONE":
    string=input()
    if string!="DONE":
        if string not in strings:
            strings.append(string)
#print(strings)
print()
print("Unique list:")
for i in strings:
    if i!="DONE":
        print(i)