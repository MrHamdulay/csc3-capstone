#Asil Motala
#MTLASI002
#Assignment 6
#Question 1

print("Enter strings (end with DONE):")     #print first instruction
list_strings=[]                             #initialize loop
while True:                                 #loop for continuous inputs
    string=input("")
    if string=='DONE': break                #sentinel value to break loop
    else:
        list_strings.append(string)         #add on to list of strings

max_len=0                                   #initialize variable
for i in list_strings:
    if len(i)>max_len:
        max_len=len(i)                      #find max length of inputs
    else: ""

print()
print("Right-aligned list:")
for j in list_strings:
    indent=max_len-len(j)                   #find indentation amount
    print(indent*" "+j)                     #right justify - easier than format