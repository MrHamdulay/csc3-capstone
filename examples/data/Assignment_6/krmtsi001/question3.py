def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    party=input("Enter the names of parties (terminated by DONE): \n")
    party_names={} #party names become a dictionary
    key_list=[] 
    while party !="DONE":
        if party not in party_names.keys():   
            party_names[party]=1
            key_list.append(party)#adding new key to the dictionary
        else:
            party_names[party]=party_names[party]+1 #adding on the value by one in the dictionary with respect to each key
        party=input() 
    print()       
 
    key_list.sort()    
    print("Vote counts:") 
    #sorted(party_names.keys())  #putting the keys in alphabetical order in dictionary
    for name in key_list:
        print(name,(10-len(name)+1)*" ","-"," ",(party_names[name]),sep="")
main()        
        
    
    
    
    




