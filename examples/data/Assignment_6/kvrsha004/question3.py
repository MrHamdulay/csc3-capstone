""" Q3 of Assignment 6: Vote counter
 KVRSHA004
 20th April 2014 """

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

i = 1
parties = []

while i == True: #input of strings
    x = input()
    if x == "DONE":
        break #end input loop
    parties.append(x)
print()

partysort = []
if parties != []:
    partysort.append(parties[0])
for j in parties: #obtain list of unique parties
    if j not in partysort:
        partysort.append(j)
partysort.sort() #sorted list of parties

print("Vote counts: ")
for k in partysort: #count votes for each party
    print("{0:<10}".format(k),"-", parties.count(k)) 