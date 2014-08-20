'''A program to count the number of votes for each political party in an election
Sandile Christopher Mahlangu
21 April 2014'''
def elections():
   '''This function takes a list of party names and counts how many votes a party has'''
   print('Independent Electoral Commission\n--------------------------------')
   
   #Creating a list and a dictionary containing the parties
   parties=[]
   parties_dictionary={}
   
   parties_request=input('Enter the names of parties (terminated by DONE):\n')
   parties.append(parties_request)
   
   while 'DONE' not in parties:
      parties_request=input('')
      parties.append(parties_request)
   parties.remove(parties[-1])
   parties=sorted(parties)
   
   #Counting the number of times a party appears in a list
   for party in parties:
      if party not in parties_dictionary:
         parties_dictionary[party]=1
      else:
         parties_dictionary[party]+=1
   #Printing the results
   results=[]
   for partyy in parties: #Making a 2 dimensional list containing partyies and their results
         if [partyy,parties_dictionary[partyy]] not in results :
            results.append([partyy,parties_dictionary[partyy]])
   print('\nVote counts:')
   for i in range(len(results)):
      
      print('%10s - %d'%(results[i][0].ljust(10),results[i][1]))         
elections()