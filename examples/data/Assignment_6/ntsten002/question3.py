#question3
#Tendani Netshitenzhe
#25April2014

#Print out headings
print("Independent Electoral Commission")
print("--------------------------------")

#Set counter to zero
count=0

#Prompt for input
parties = input("Enter the names of parties (terminated by DONE):\n")

#Create empty dictionaries
mylist= {}
myparty={}

#Populate mylist dictionary
while parties != "DONE":
    mylist[count] = parties
    parties = input("")
    count+=1

#Populate myparty dictionary
for k in range(count):
    party=0
    i=1
    for i in range(count):
        if mylist[k] == mylist[i]:
            party+=1
    myparty[mylist[k]]=party
    
print("\nVote counts:")
#Display sorted dictionary
for j in sorted(myparty):
    print(j.ljust(10),"-", myparty[j])

    
        
    
    