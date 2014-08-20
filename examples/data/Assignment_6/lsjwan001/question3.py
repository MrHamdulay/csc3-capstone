# Program count number of votes for each political party
# Wandile Lesejane
# 23 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
party=input("Enter the names of parties (terminated by DONE):\n")
parties=[]

# put all names in a list
while party!="DONE":
    parties.append(party)
    party=input()
#count number of unique words
count={}
listp=[]
for i in parties:
    count[i]=count.get(i,0)+1
# list and sort unique words
listp=list(count.keys()) 
listp.sort()
#print results in required format
print()
print("Vote counts:")
for i in listp:
    space=" "*(9-len(i))
    print(i,space,"-",count[i])
    
    