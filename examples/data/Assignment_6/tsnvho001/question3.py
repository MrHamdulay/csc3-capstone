#Program to count the number of votes for each political party in an election
#Tsanwani Vhonani
#21 April 2014

def elections():
   print ("Independent Electoral Commission")
   print ("--------------------------------")
   #get input from user
   print ("Enter the names of parties (terminated by DONE):")
   
   votes={}
   party=""
   #while the the elections are not done,get more votes from users
   while party!='DONE':
      party=input("")
      #if the elections are not done, if the party is has not been voted for, count the vote once
      if party!='DONE':
         if not party in votes:
            votes[party]=1
         #if the party has been voted for,add 1 vote to the votes already in
         else:
            votes[party]=votes[party]+1
   
   print ("\nVote counts:")
   for party in sorted(votes.keys()):
      #print the name of the party and its votes
      print ("{:<10} - {}".format (party,votes[party]))
      
elections()
     