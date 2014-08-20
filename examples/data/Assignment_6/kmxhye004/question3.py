#Assignment 6
#Question 3
#Helin Kim

print("Independent Electoral Commission")
print("--------------------------------")

vote_parties=[]
votes = input("Enter the names of parties (terminated by DONE): \n")


while votes != "DONE":
    vote_parties.append(votes)
    votes = input("")

count = {}
    

for parties in vote_parties:
    if not parties in count:
        count[parties] = 1
    else:
        count[parties] += 1


print()
print("Vote counts:")
for parties in sorted(count):
    print ("{0:<11}{1}{2:2}".format(parties, "-", count[parties]))