#Question 3 
#Political party vote counting
#By: Dean de haast

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    party =input("Enter the names of parties (terminated by DONE):\n")
    
    parties=[]
    #Inserting the first item into the list
    if party != "DONE":
        parties.append([party,1])
    #Setting the end condition.
    while party != "DONE":
        party =input()
        found =False
        
        #Checking if the political party has been entered    
        for i in range(len(parties)):
            if party == parties[i][0]:
                found = True
                #Adding one to the count of that party if it is found
                parties[i][1] =parties[i][1] +1
                
                
        if party =="DONE":
            found =True
        # Adding the Political Party if not found    
        if found==False:
            parties.append([party,1])
    parties.sort()        
    #Printing the results            
    print()            
    print("Vote counts:")
    for i in range(len(parties)):
        print("{0:<10}".format(parties[i][0]),"-",parties[i][1])
main()