"""shriya roy
4 April 2014
program to calculate vote counts of certain parties"""


def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    #create empty list
    list_of_parties= []
    #get input from user 
    parties= input("Enter the names of parties (terminated by DONE):\n")
    
    while parties!= "DONE" :
        list_of_parties.append(parties)
        parties= input("")
    

    
        
        
    #create an empty dictionary    
    D= {}
    
    print()
    print("Vote counts:")
    #count the number of votes for each party
    for name in list_of_parties:
        if not name in D:
            D[name]=1
        else:
            D[name]+=1

     #print the votes   
    for name in sorted(D):
        output="{0:10}".format(name)
        
        print(output, "-", D[name])
        
main()
    