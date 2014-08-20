print("Independent Electoral Commission")
print("--------------------------------")

prompt=input("Enter the names of parties (terminated by DONE):\n")
parties=[]
vote_dictionary={}
parties.append(prompt)
while prompt!="DONE":
    prompt = input("")
    parties.append(prompt)
parties.remove("DONE")
for name in parties:
    if name in vote_dictionary:
        vote_dictionary[name] +=1
        
    else:
        vote_dictionary[name] = 1
print()        
print("Vote counts:")
for name in sorted (vote_dictionary.keys()):
    print ("{0:<10}".format(name),"-",vote_dictionary[name])


    
    
    
    
