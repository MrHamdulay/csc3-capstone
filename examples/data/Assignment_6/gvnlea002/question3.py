""" Voting program
Leandra Govender
22 April 2014"""

print("Independent Electoral Commission")             #display heading
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")          #print instruction

vote_list= []
while True:
    x= input()
    if x=="DONE":break                                #loop stops when "Done is entered
    vote_list.append(x)                               # input is added to list
    
print()
print("Vote counts:")
parties = []
if vote_list != []:
    for i in vote_list:
        if i not in parties:
            parties.append(i)

parties.sort()

for j in parties:
    print("{0:<10}".format(j), "-", vote_list.count(j))