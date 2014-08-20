# A program that counts the number of votes for each political party in an election.
#gillian wachira
#26th April 2014
print("Independent Electoral Commission")
print("--------------------------------")
listA=[]
y=input("Enter the names of parties (terminated by DONE):\n")


while y!="DONE":
        listA.append(y)
        y=input("")
        
print()       
print("Vote counts:")
counter = {}

for i in listA:
        if not i in counter:
                counter[i]= 1
        else:
                counter[i]+= 1
                
for i in sorted(counter):
        print(i+" "*(10-len(i)),"-",counter[i])
