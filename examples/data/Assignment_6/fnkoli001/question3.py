print("""Independent Electoral Commission
--------------------------------""")

#Get input
parties = []

input_string = input("Enter the names of parties (terminated by DONE):\n")
parties.append(input_string)

while input_string != "DONE":
    input_string = input("")
    parties.append(input_string)

parties = parties[:-1]

#Add new parties to a dic and increase a the count for each
parites_dic = {}

for party in parties:
    if party in parites_dic:
        parites_dic[party] += 1
    else:
        parites_dic[party] = 1

#Display results
print()
print("Vote counts:")

for key in sorted(parites_dic):
    print(key+" "*(11-len(key))+"- "+str(parites_dic[key]))