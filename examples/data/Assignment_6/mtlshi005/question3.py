#Shivaan motilal
#22 APRIL 2014

#prints heading

print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

#Obtain input from voter

listp=[]
party=""
while party!="DONE" and party!='DONE':
      party=input()
      if party!="DONE" and party!='DONE':
            listp.append(party)
            
#Count number of votes and store in a dictionary


counter={}             #create dictionary
for party in listp:              
      if not party in counter:        
            counter[party] = 1
      else:
            counter[party] += 1
            
print()

#display results

print("Vote counts:")

output="{0:<10} - {1:}"
COUNT=0
for key in sorted(counter):
      print(output.format(key,counter[key]))
      COUNT+=1

            
              
      #party=str(party)
      #listp+=party
      #print(listp)
#print(party)      
#print(listp)
      
