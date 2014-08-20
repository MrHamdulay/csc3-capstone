'''Program to count and display election votes
Tinotenda Chevmura (CHMTIN004)
20 April 2014'''

#_____________Program starts here____________#

print("Independent Electoral Commission\n--------------------------------")

#create an empty list

parties = []

#obtain the list of party names and votes
#and each party to a list

name = input("Enter the names of parties (terminated by DONE):\n")
name = name.upper()
if name != "DONE":
    parties.append(name)
    
while name != "DONE":
    name = (input()).upper()
    parties.append(name)

#delete the "DONE" from the list
#list the parties in alphabetis order

if len(parties) > 1:
    del parties[len(parties)-1]
    parties.sort()

#find the occurance of each element in parties
# create a new list without repetition of any aprties

names = []
for party in parties:
    if party not in names:
        names.append(party)

#create an empty list for counting number of votes
#go through [parties] and count the occurence of each party, adding to the counter list

counter = []

for i in names:
    count1 = 0
    for j in parties:
        if j == i:
            count1+=1
    counter.append(count1)

#print the results only if there is at least 1 vote

print("\nVote counts:")
for i in names:
    position = names.index(i)                   #retrieve position of the current party
    partyF = "{0:<10}".format(i)                #the current party is formated here, left justified in column width 10
    partyF = partyF.lower()
    print(partyF,"-",counter[position])
        
#___________________________Program Ends Here________________________________