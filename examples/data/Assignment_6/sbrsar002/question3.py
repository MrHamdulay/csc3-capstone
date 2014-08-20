""" a program to count the number of votes for different parties
Sarayn Subroyen
22 April 2014"""

def main():
    print("Independent Electoral Commission")
    print("-"*32)
    
    #create list of parties
    names = []
    name = input ("Enter the names of parties (terminated by DONE):\n") #DONE is a sentinel
    #name_list=name.split(" ")

    while name != "DONE":          #add names to list
        names.append (name)
        name = input ("")

    print()
    print("Vote counts:")  
    counter = {}           #create a dictonary
    
    for name in names:             #add votes for each party
        if not name in counter:
            counter[name] = 1
        else:
            counter[name] += 1
    
    for name in sorted(counter):   #sort in alphabetical order
        print ("{0:<10}".format(name),"-",counter[name])    #format to a width of 10
        
main()
    