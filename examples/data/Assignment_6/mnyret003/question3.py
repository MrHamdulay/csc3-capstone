# A program that counts the number of votes for each political party in an election.
# Retselisitsoe Monyake
# 23/04/14

print("Independent Electoral Commission")
print("--------------------------------")
mylist=[]# empty list to enter names of parties
parties=input("Enter the names of parties (terminated by DONE):\n")
while parties!="DONE":
        mylist.append(parties)# entering names into a list
        parties=input("")

        
print()       
print("Vote counts:")

# start with zero counters
counter = {}

# count words and add new words as they are encountered
for word in mylist:
    if not word in counter:
        counter[word] = 1
    else:
        counter[word] += 1
        
# print out counters
for word in sorted(counter):
    print (word+" "*(10-len(word)),"-",counter[word])
    
    
    
        



