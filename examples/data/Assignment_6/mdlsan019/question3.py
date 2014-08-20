'''SANELE MDLALOSE
   MDLSAN019
   Votes
   Assignment6,Question3
   21 April 2014'''


def votes():
        print("Independent Electoral Commission")
        print("--------------------------------")
        parties = input("Enter the names of parties (terminated by DONE):\n")
        Parties_list = []  #Create an empty list
        
        if parties!='DONE':
                while True: 
                        Parties_list.append(parties)  #Append each item into Parties_list
                        parties = input("")     #Input more names
                        if parties == "DONE":   
                                print()            #Spacing after the loop
                                break
                           
                        
                           
        else:
                print()

        Parties_list1=list(set(Parties_list))    #Eliminate repitition of items in a list
        Parties_list1.sort()         #Sorting the new list

        print("Vote counts:")
        for item in Parties_list1:
                x=Parties_list1.index(item)  #Acquiring the index of the item
    
                print("{0:<10}".format(item),"-",Parties_list.count(item))  #Output a list of counted items
votes()    
    

    

    

    
   