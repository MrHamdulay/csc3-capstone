#Program to count the number of votes for each political party in an election.
#Ayesha Marcus
#22/04/2014
def main ():
  sInput = "" 
  parties = []
  partyCount = {}
  
  print ("Independent Electoral Commission")
  print ("--------------------------------")
  print ("Enter the names of parties (terminated by DONE):")
  while sInput != "DONE":
    sInput=input("")
    if (sInput != "DONE"):
      parties.append(sInput)
  else:
    print("")
    
  
  for f in sorted(parties, reverse=False):
    #print(f)
    if f in partyCount:
      #print("FOUND key for ",f)
      partyCount[f] = int(partyCount[f]) + 1
    else:
      #print("No key for ",f)
      partyCount[f] = 1
      #partyCount[f] = int(partyCount[f]) + 1
    
  print("Vote counts:")
  for k, v in sorted(partyCount.items(), reverse=False):
    print(k.ljust(10),'-',v)
  
if __name__ == "__main__":
  main()
