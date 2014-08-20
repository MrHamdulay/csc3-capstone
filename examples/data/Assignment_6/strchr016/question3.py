"""Counting votes
Christopher Sterley
20/04/2014"""

print("Independent Electoral Commission")
print("--------------------------------")

#Get party names for program
party_name=input("Enter the names of parties (terminated by DONE):\n")

party_list=[]
party_number_list=[]

#create lists to be used to counte votes and keep track of parties used
while party_name!="DONE":
    if party_name in party_list:
        party_number_list.append(party_name)
        party_name=input("")

    else:
        party_list.append(party_name)
        party_number_list.append(party_name)
        party_name=input("")

print()

#sort party list
party_list.sort()

#print the party it respective votes
print("Vote counts:")
for i in range(len(party_list)):
   print("{0:10}".format(party_list[i]),"-",party_number_list.count(party_list[i]))