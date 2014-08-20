def cntparty():                                                 
    p=0                                                         
    listy=[]
    print("Enter strings (end with DONE):")
    while p != "DONE":                                           
        p = input()                                              
        if p == "DONE":                                         
            continue
        else:                                                    
            if p in listy:
                listy=listy                                    
            else:
                listy.append(p)
    
    print("\nUnique list:")
    for i in range (len(listy)):
        print(listy[i])
cntparty()