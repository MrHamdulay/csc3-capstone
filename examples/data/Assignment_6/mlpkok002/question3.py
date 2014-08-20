print("Independent Electoral Commission")
print("--------------------------------")
    
names=[] #create empty list
name=input("Enter the names of parties (terminated by DONE):\n") #prompt for name

if name!="DONE": #if user does not enter DONE first:
    while name!="DONE":
        names.append(name)#fill list with names until user enters DONE
        name=input("") #allows user to keep entering until user types DONE
    names.sort() #sort the list of names     
   
    print("")
    print("Vote counts:")
    names_count=[] #create empty list
    for i in names: #loop over (sorted) names:
        if i in names_count:
            continue  #if name already in names_count, do not add it again!
        names_count.append(i) #fill empty list with names
        count=names.count(i) #count the number of times each name occurs
        gap=10-len(i) #create variable gap:
        print(i+" "*gap,"-", count) #print name, the number of spaces depeding on its length and the number of times it occurs 
        
        

else:         #if user enters DONE first 
    print("")
    print("Vote counts:")
    print("")
    
        