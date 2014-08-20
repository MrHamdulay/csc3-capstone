#program to count votes
#kiyarah pillay
#24 april 2014

print("Independent Electoral Commission")
print("--------------------------------")

party_list= []
candidates={}

parties=input("Enter the names of parties (terminated by DONE):\n")

#use DONE as the sentinel value
while parties != "DONE":
    party_list.append(parties)
    parties=input ("")
#create a dictionary
for something in (party_list):
    if not something in candidates:
        candidates[something]=0
    candidates[something]+=1
print()
print ("Vote counts:")
#allignment
y = "{0:<10}"
for something in sorted (candidates):
    print(y.format(something),"-",candidates[something]) 
        