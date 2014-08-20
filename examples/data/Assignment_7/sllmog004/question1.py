"""Assignment 7 Q1
Yaseen Sulliman
29 April 2014"""

array=[] #create list 
string=input("Enter strings (end with DONE):\n") #request user for input
array.append(string) #add to list
while string!="DONE": 
    string=input("")
    array.append(string)
    
newlist=[] #create newlist
for x in array:
    if x not in newlist:
        newlist.append(x) #add each element in old list to newlist

print()
print("Unique list:")        
for i in range(len(newlist)-1):
    print(newlist[i])