def Mr_Listy():
    i=input("Enter strings (end with DONE):\n")
    listy={}
    ordlist=[]
    while i!="done" and i!= "DONE":
        if i in listy:
            listy[i]+=1
        else:
            listy[i]=1
            (ordlist).append(i)
        i=input("")
    print("\nUnique list:")
    for i in (ordlist):
        print(i)
Mr_Listy()