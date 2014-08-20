
#empty lists to collect the strings
stringslist=[]
uniquestrings=[]

x=0
strings=input("Enter strings (end with DONE):\n")
if strings=="DONE":
        while x:
                break
        
else:
        stringslist.append(strings)
#loop that allows indefinite input of values
while strings != "DONE":
        strings=input("")
        if strings!= "DONE":
                stringslist.append(strings)
print()
print("Unique list:")

for i in range(len(stringslist)):
        #this check examines whether the word in list:strings has already been seen.
        #If so, it is skipped, as it is already a unique input.
        if stringslist[i] in uniquestrings:
                continue        
        else:
                
                uniquestrings.append(stringslist[i])
                print(stringslist[i])
               
                
        
        
                

                