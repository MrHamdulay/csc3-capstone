"""program to take in a list of parties and count the votes for each party
joshua gullan
22 april 2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#get first item for list
x=input("Enter the names of parties (terminated by DONE):\n")

#create empty list for the parties
parties=[]

#get party list, sentinel is "DONE". Append is first due to the first input being above, which is before the loop.
while x!="DONE":
    parties.append(x)
    #this input means that there is no prompt and the user can enter a party, hit enter and enter another one until they type "DONE"
    x=input()

#appends last input before "DONE"
if x!="DONE":
    parties.append(x)
#sort the list of parties 
parties.sort()
print("\nVote counts:")


list2=[]

#populates list2 with only one party name of each
for i in parties:
    if i in list2:
        continue
    else:
        list2.append(i)

numbers=[]

#runs through each party name and counts number of repeats in the full list entered by user
for i in list2:
    x=parties.count(i)
    numbers.append(x)

#prints each party name within 10 column and prints corresponding number
for i in range(len(list2)):
    print(list2[i].ljust(11," "), "- ",numbers[i], sep="")
    

    
