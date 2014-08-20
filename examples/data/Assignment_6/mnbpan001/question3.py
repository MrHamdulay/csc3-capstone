"""Program to count number of votes
Pankaj Munbodh
20 April 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#Create dictionary and assign value to first party
partyname=input("Enter the names of parties (terminated by DONE):\n")
partdict={}
if partyname !="DONE":
    partdict[partyname]=1

#Sentinel loop which keeps asking for input from user until "DONE" is entered
#Integrate other parties to dictionary and assign values to keys according to number of votes
    while True:
        partyname=input("")
        if partyname=='DONE': break
        if partyname in partdict:      #if party already exists in dictionary, add one vote
            partdict[partyname]+=1
        else:                          #else create entry for party with a value of 1
            partdict[partyname]=1

    print()
#Output
    print("Vote counts:")
    parties=list(partdict.keys())  #get list of keys(party names) in dictionary
    parties.sort()                 #sort list in alphabetical order 

#Insert party name in field of required width left-justified and value alongside
    for party in parties:
        print("{0:<10}".format(party),"-",partdict[party])

#output for exception
else:
    print()
    print("Vote counts:") # To cater for exception when sentinel is given right at start of program
    

#useful info : list(dict.values())