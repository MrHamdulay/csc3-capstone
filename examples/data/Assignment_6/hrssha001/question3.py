# Program to count votes of parties not yet specified
# Shane Horsley
# 20 April 2014
print("Independent Electoral Commission\n"+32*"-")
party=input("Enter the names of parties (terminated by DONE):\n") # ask for party name 
print()
PL=[] # list for first occurance of party name
PL2=[]# list for duplicates
while party != "DONE": #keep asking for party names
    if  party not in PL: # if its the first occurance
        PL.append(party)
    else: # if party has already been mensioned
        PL2.append(party)
    party = input()
PL.sort() # to get alphabetical order for later printing
print("Vote counts:")
for i in PL: # iterates over every word in the first list
    count = PL2.count(i) # counts nmber of times word comes up in 2nd list
    print("{:<10}".format(i)+" -",count+1) # plus 1 is because of the 1 in the first list 