print('Independent Electoral Commission')
print('--------------------------------')
parties=[]
party=input("Enter the names of parties (terminated by DONE):\n")
while party!="DONE":
     parties.append(party)
     party=input("")
print()
print("Vote counts:")

partynumbers={}
if len(parties)!=0:
     for party in parties:
          counts=parties.count(party)
          partynumbers[party]=counts
     
     for part in sorted(partynumbers.keys()):
          gap=10-(len(part)-1)
          print(part+' '*gap+'-',partynumbers[part])
          
     


     
