#a program to count the number of votes for each political party in an election
#Ali Goldstein
#23 april 2014

#prompt the user to enter names of parties
print("Independent Electoral Commission")
print("--------------------------------")
parties=input("Enter the names of parties (terminated by DONE): \n")

#creating an empty list
list=[]

#it goes through the list and adds the party name onto the end of the list
#when the user enter "DONE", the while loop will stop 
while parties!="DONE":
    list.append(parties)
    parties = input("") 

counters={}

#goes through the list and counts the number of times each party occurs
for word in list:
    if not word in counters:
        counters[word]=0
    counters[word]+=1
    
#prints each party and the corresponding vote count  
print()
print("Vote counts:")
for word in sorted(counters.keys()):
    print(word, (10-len(word))*' '+'-',counters[word])
