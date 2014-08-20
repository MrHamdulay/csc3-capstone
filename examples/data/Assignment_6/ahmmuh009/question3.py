def voting():
    list_1=[]
    dict_1={}
    list_2=[]
    print("Independent Electoral Commission\n--------------------------------")
    vote=input("Enter the names of parties (terminated by DONE):\n")
    while vote!="DONE":
        list_1.append(vote)
        vote=input("")
        if vote=="DONE":
            break
    print()
    for i in list_1:
        dict_1[i]=list_1.count(i)
    print("Vote counts:")
    for key in dict_1.keys():
        list_2.append(key)
    list_2.sort()
    for key in list_2:
        print("{0:10}".format(key),end=" ")
        print("-",dict_1[key])

        
voting()