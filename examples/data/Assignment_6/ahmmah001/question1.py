'''Program to print a right-aligned list
Mahnoor Ahmed
23 April 2014'''

slist=[]
string=input("Enter strings (end with DONE):\n")
slist.append(string)
slength=len(string)
while string != "DONE":
    string=input("")                                          
    slist.append(string)                                   #adds every string to list
    if len(string)>slength and string != "DONE":           #calculates the length of the longest string
        slength=len(string)
        
del slist[-1]                                              #deletes the last item from the list because its "DONE"
print("\nRight-aligned list:")

for i in range(len(slist)):
    item= slist[i]                                         #retrieves the item at each position in list
    print(" "*(slength-len(item)),item,sep="")             #prints a right aligned list by buffering the LHS with " "