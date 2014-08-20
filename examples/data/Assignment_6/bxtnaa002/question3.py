# question3.py
# author: bxtnaa002

print("Independent Electoral Commission"+"\n"+"--------------------------------")

# create a list of parties and DONE is inputed to terminate the growth of the list
parties = []
inputs= input("Enter the names of parties (terminated by DONE):\n")
while inputs != "DONE":
    parties.append(inputs)
    inputs = input("")
    
counter = {} #create a dictionary which will contain the each party as a key and the number of its occurences as the value for that key
for party in parties:
    if not party in counter: #this is if the party does not already exist as a key in the dictionary
        counter[party] = 1
    else:
        counter[party] += 1

print("\nVote counts:")
for party in sorted(counter): # sort the dictionary
    a = "{0:<10}".format(party) # this is for alignment
    print (a+" - "+str(counter[party])) 