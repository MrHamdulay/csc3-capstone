#shane horsley
#program to print first occurance of words

string = input("Enter strings (end with DONE):\n")
print()
uniquelist=[]
while string != "DONE": #add string to list only if it is not there already
    if  string not in uniquelist: 
        uniquelist.append(string)
    string = input()
print("Unique list:")
for i in uniquelist: #print every strng on a new line
    print(i)