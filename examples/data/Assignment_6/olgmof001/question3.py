"""Tofunmi Olagoke
OLGMOF001
23rd April 2014
Voting program"""

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    print('Enter the names of parties (terminated by DONE):')
    votes= []
              
    #adding votes to list
    while True:
        vot=input('')
        votes= votes+[vot]
            
        if vot=="DONE":
            break
    wo=votes[0:-1] #remove done from list
    wo.sort()#sorts list in alphabetical order
    
    test=[]
    
    print()
    print("Vote counts:")
    
    #Goes through list to count the occurance of each party
    for i in wo:
        if i not in test:
            print(i,(10-len(i))*" "+"-",wo.count(i))
            test=test+[i]
        
main()