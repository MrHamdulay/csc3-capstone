parties={}
print("Independent Electoral Commission")
print("--------------------------------")
votes=input("Enter the names of parties (terminated by DONE):\n")
while votes != 'DONE' :
      if votes in parties:
            parties[votes]=parties.get(votes)+1
            votes=input("")
      else:
            parties[votes]=1
            votes=input("")
x = sorted(list(parties.keys()))
print("")
print("Vote counts:")
for k in x:
            A="{:<10}".format(k)
            print (A, parties[k],sep=" - ")