"""Program to count the votes of political parties
Shane Robinson
20 April"""

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):\n")
name = input()
parties = []

while name!='DONE':
    parties.append(name)
    name = input()

parties.sort()  #orders list
print("Vote counts:")

while parties!=[]:
    party = parties[0]
    num = parties.count(party)  #count occurrences of first item in list
    for i in range(num):
        parties.remove(party)   #remove all occurrences of first item
    print(party, " "*(9-len(party)), "-", num)