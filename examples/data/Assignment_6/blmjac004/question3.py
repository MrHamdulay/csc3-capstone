"""count number of votes per party
Jacqueline Blomendahl
23/04/2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#getting input and creating an empty list and dictionary
parties=input("Enter the names of parties (terminated by DONE):\n")
Lists= []
Lists.append(parties)
dictionary= {}

#adding inputs to list
while parties != "DONE":
    parties=input()
    Lists.append(parties)
del Lists[-1]

#sorting list and adding to dictionary
Lists.sort()
for i in (Lists):
    if not (i in dictionary.keys()):
        dictionary[i] = Lists.count(i)

#sorting dictionary and printing output
sorted_dict=sorted(dictionary)
print()
print("Vote counts:")
for i in sorted_dict:
    print(i.ljust(10), "-", dictionary[i])
