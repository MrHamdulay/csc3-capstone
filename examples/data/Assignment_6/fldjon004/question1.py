#jono field
#24 April
#question 1

name=input("Enter strings (end with DONE):\n")
if name == "DONE": #if user immediately inputs DONE, return an empty list
    firstnames = []
else:
    firstnames = [name] #otherwise, create list with first name in it
    namelength = len(name) #calculates length of first name
    names = "" #empty string
    while names != "DONE": #sentinel loop is being created (sentinel = "DONE")
        names=input()
        firstnames.append(names) #add name to list
        namelength2 = len(names) #calculates length of new name
        #finding max length
        if namelength2 > namelength: 
            namelength = namelength2
    firstnames.remove("DONE") #remove "DONE" from list
print()
print("Right-aligned list:")
for i in firstnames:
    print(i.rjust(namelength)) #prints names right-aligned
    
            
    
    
        
