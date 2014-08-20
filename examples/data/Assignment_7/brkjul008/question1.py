#ordered strings
#julia breakey
#1 may 2014

#create strings list
strings=[]
string=input("Enter strings (end with DONE):\n")
while string!="DONE":
    strings.append(string)
    string=input("")

#print list of unique values
print("")
print("Unique list:")    
unistrings=[]
for i in strings:
    if i in unistrings:
        continue
    else:
        print(i)
        unistrings.append(i)