# David Onyango
#count the number of votes of a political party in an election
#enter the names of the political parties (print statment)
  
print("Independent Electoral Commission \n--------------------------------\nEnter the names of parties (terminated by DONE):\n")

#change the strings into lower case 
    #names = input().lower()
lst = []
dictionary = {}
a = 0
names = ""
nlis = []
    
#sequence of parties (may be repeated names)
while names != "DONE":
    names = input()
    lst.append(names)
    #use dictionary to show unique parties
    dictionary[names] = a
    a += 1
print("Vote counts:" )

#sorting list
lst.sort()

#add to list
for a in dictionary:
    nlis.append(dictionary[a])
#deleting value done
del nlis[-1]


#format party names with with = 10. (make assumption)
#loop while deleting items in the lis
for i in range(len(nlis)):
    count = 0
    count = lst.count ( lst[0])
    gap = 11 - len( lst[0])
    
    print(lst[0] + gap *' '+'- ' + str((count)))
    for i in range (count):
        del lst[0]
    
                            
