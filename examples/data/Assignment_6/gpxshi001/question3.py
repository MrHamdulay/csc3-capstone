#GPXSHI001
#ASS 6
#VOTE COUNTER
#Q3


def party_time():
    
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    new_list=[]
    for_prty=""
    prty=[]
    na=0
    while for_prty!="DONE":             
        for_prty=input("")
        
        if for_prty!=("DONE"):
            prty.append(for_prty)
    
    for names in range(len(prty)):
        
        if prty[names] in new_list:  #does Nothing
            na+=1
            
        else:
            new_list.append(prty[names]) #adding prty_names to a new list so we can print single party names
            
    new_list.sort()
    print("\nVote counts:") 
    
    for f in range(len(new_list)):
        print(new_list[f],(9-len(new_list[f]))*" ","-",prty.count(new_list[f]))
    
    
    
    
    
party_time()
