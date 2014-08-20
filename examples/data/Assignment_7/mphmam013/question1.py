"""Mphuthi Mamorena
assignment 7
question 1
27 april 2014"""

#A LIST ENTERD BY THE USER
strings=[]
string=input("Enter strings (end with DONE):\n")

while string!='DONE':
    strings.append(string)
    string=input()
print()
print("Unique list:")

#CREATING ANOTHER LIST WITHOUT DUPLICATES
realstrings=[]
if len(strings)!=0:
    for i in range(len(strings)):
        if strings[i] in realstrings:
            continue
        else:
            realstrings.append(strings[i])


    # PRINTING A LIST WITHOUT DUPLICATES
    for rstring in realstrings:
        print(rstring)
        
    
    
