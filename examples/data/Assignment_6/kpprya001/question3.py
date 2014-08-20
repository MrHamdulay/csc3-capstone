print("Independent Electoral Commission\n--------------------------------")
names = input("Enter the names of parties (terminated by DONE):\n")
#create array for list of parties
lists = []

#while user hasnt terminated program, do the following
while names != ("DONE"):
    lists.append(names)
    names = input("")
    
#create dictionarty to hold votes   
counter ={}
#work out the votes for each party - if party name is in dictionary, add one.If not then add name and add 
   
for word in lists:
    if not word in counter:
        counter[word] = 1
        
    else:
        counter[word] += 1


#sort the list and then print the results       
lists= sorted(lists)
print()
print("Vote counts:")
for word in sorted(counter):
    print (word," "*(11-len(word)),"- ",counter[word],sep="")
    





    

