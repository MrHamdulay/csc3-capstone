""" vote counter for names of parties
Tayla George
22 April 2014"""

def partycounts():
    print("Independent Electoral Commission")
    print("--------------------------------")
    
    #creating a list with the party names
    names = []
    name = input ("Enter the names of parties (terminated by DONE):\n") 
    

    while name != "DONE":          #add the names entered to list
        names.append (name)
        name = input ("")

    print()
    print("Vote counts:")  
    counter = {}          
    
    for name in names:             #calculate votes for each party
        if not name in counter:
            counter[name] = 1
        else:
            counter[name] += 1
    
    for name in sorted(counter):   #sort in alphabetical order
        print ("{0:<10}".format(name),"-",counter[name])    #format to a width of 10
        
partycounts()
    