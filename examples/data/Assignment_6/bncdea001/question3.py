#Program to count party votes
#Dean Bunce
#21 April 2014

def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    
    #Create list
    name_list=[]
    
    #Get each name
    name=input("Enter the names of parties (terminated by DONE):\n \n")
    while name!="DONE":
        name_list.append(name)
        name=input("")
        
    #print(name_list)
    
    
    name_list.sort()
    
    #print(name_list)
   
    #Make a list of parties and their votes
    print_list=[]
    
    print("Vote counts:")
    #Now consider the sorted list of votes.
    for name in name_list:
        #Count each party's votes
        votes=name_list.count(name)
        #Give a template for how they are to be printed
        formatted_result="{0:<11}{1}{2}".format(name,"- ",votes)
        #If a party's template name is not on the list-add
        if formatted_result not in print_list:
            print_list.append(formatted_result)
        elif formatted_result in print_list: continue
    #print(print_list)
    
    #Print each name and votes 
    for name in print_list:
        print(name)
        
    
   
    
main()