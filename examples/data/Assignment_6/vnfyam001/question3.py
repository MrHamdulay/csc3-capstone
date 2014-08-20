"""count votes
yamkela venfolo
24 April 2014"""

from collections import OrderedDict

print("Independent Electoral Commission\n--------------------------------")
xParties=input("Enter the names of parties (terminated by DONE):\n")
Dlist=[]
names=""
dictionary={}
dalpha=[]  
#keeps on looping until a user enters done
while xParties != "DONE":  
    names=names+" "+xParties 
    xParties=input() 
if names!="":   
    names=names[1:] 

    Dlist=names.split(" ")    

    for i in range(len(Dlist)):
#this is a boolean that checks if the party is in the dictionary   
        rt = Dlist[i] in dictionary
#checks if the boolean i strue or false    
        if rt:
            dictionary[Dlist[i]]=dictionary[Dlist[i]]+1
        else:
            dictionary[Dlist[i]]=1
            dalpha.append(Dlist[i])
    
#dictionary = OrderedDict(dictionary)
    high=0
    for i in dictionary:
#Find the name in the dictionary that has longest len  
        if(len(i)> high):
            high=len(i)
#sort the strings in the array in alphabetical order     
    dalpha.sort()

    #print the strings in the sorted order
print("\nVote counts:")
for i in sorted(dalpha):
        print(i,(9-len(i))*" ","-",dictionary[i])
   
