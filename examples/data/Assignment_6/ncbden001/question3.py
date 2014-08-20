#Program to keep track of votes
#Denzel Ncube
#23 April 2014

print("Independent Electoral Commission \n-------------------------------- \nEnter the names of parties (terminated by DONE):\n")
#default values for variables
lst = []
newlst = []
a = 0
dicto = {}
party = ""

#Adding to the different lists
while party != "DONE":
        party = input()
        lst.append(party)
        dicto[party] = a
        a+=1
print("Vote counts:")




#Deleting "DONE"
del lst[-1]
#Sorting the list
lst.sort()

#Adding to list
for a in dicto:
        newlst.append(dicto[a])
#Deleting "DONE"
del newlst[-1]

#Looping for the number of unique parties
for i in range(len(newlst)):
        count = 0
        #Counting votes
        count = lst.count(lst[0])
        #Printing in correct format
        gap = 11-len(lst[0])
        print(lst[0]+gap*' '+'- '+str(count))                
        for i in range(count):
                del lst[0]
                
        
      
