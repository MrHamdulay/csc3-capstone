#Sheldon Kisten
#using lists to count votes
#22 April 2014

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

vote_list= [] #empty list
while True:
    a= input()
    if a=="DONE":break
    vote_list.append(a)
    
print()
print("Vote counts:")
parties = []
if vote_list != []: #ensure no syntax error
    for i in vote_list:
        if i not in parties:
            parties.append(i)

parties.sort()

for j in parties:
    print("{0:<10}".format(j), "-", vote_list.count(j))