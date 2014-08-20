#maisha ivha
#24/04/2014
# program to count the number of votes for each political party


print ("Independent Electoral Commission")
print ("--------------------------------")
print ("Enter the names of parties (terminated by DONE):")

def main ():
  s= "" 
  parties = []
  Dparties= {} #a dictionery for parties that have been sorted
  
 #a loop that asks for input/name of parties and breaks when the sentinel "DONE" is typed in
  while s!= "DONE":
    s=input("")
    if s!="DONE":
      parties.append(s)#adding the party name to a list of parties
        
  
  for i in sorted(parties, reverse=False):#Sorting the list of parties in alphabetical order
    
    if i in Dparties:
          Dparties[i] = int(Dparties[i]) + 1
    else:
      Dparties[i] = 1
      
    
  print("\nVote counts:")
  for i, counts in sorted(Dparties.items(), reverse=False): #linking the party with the number of votes 
    print(i.ljust(10),'-',counts)#PRINTING THE PARTY AND ITS VOTES COUNTS
main()
