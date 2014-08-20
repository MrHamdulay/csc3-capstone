"""Program to count votes
Tyrone Arnold
24/04/2014"""

def vote_count():
        
        print("Independent Electoral Commission")
        print("--------------------------------")
        
        candidate_list=[]
        list_of_names=[]
        newcandidates={}
        x=0
        party_name=input("Enter the names of parties (terminated by DONE):\n")
        if party_name=="DONE":
                while x:
                        break
                
        else:
                candidate_list.append(party_name)
        
        while party_name != "DONE":
                party_name=input()
                if party_name!= "DONE":
                        candidate_list.append(party_name)
        print()
        print("Vote counts:")
        candidate_list.sort()
        
        for i in range(len(candidate_list)):
                if candidate_list[i] in list_of_names: #checks if candidate name has been counted
                        continue        
                else:
                        x=candidate_list.count(candidate_list[i])
                        list_of_names.append(candidate_list[i])
                        print("{0:<10}". format(candidate_list[i]),"-",x)   
vote_count()