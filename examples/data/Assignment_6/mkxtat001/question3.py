#Tato Moaki MKXTAT001
#Program to simulate the Idependent Electoral Commission
#4/21/2014

#Tato Moaki MKXTAT001
#Program to simulate the IEC
#4/21/2014
def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    parties_list = [] #create an empty list     
    
    flag = False    
    while not flag:
        party_name = input()
        if(party_name == "DONE"):
            flag = True
        else:
            parties_list.append(party_name)#add party names to list end to end
            
    
    #keep count of occurences of an element in a list then convert it to a set and change party_list into a dictionary    
    party_list = dict([(i, parties_list.count(i)) for i in set(parties_list)])
    
    #set party_list from dictionary to a list and sort 
    party_list = list(party_list.items())
    party_list.sort()
    
    print("\nVote counts:")
    #display the dictionary keys and their value
    for j in party_list:
        print (("{0:<11}").format(j[0]),"- ", j[1],sep="")
            
if __name__=="__main__":
    main()