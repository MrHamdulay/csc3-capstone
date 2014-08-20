"""program to count votes
nasonkwe hampwaye
2014.04.21"""
def electrol_commission():
    print("Independent Electoral Commission")
    print("-"*32)
    names=[]
    names_input=input("Enter the names of parties (terminated by DONE):\n")
    while names_input!="DONE":
        names.append(names_input)
        names_input=input("")
    #find unique things
    count={}
    for i in names:
        count[i]=count.get(i,0)+1
    #making list
    names_new=list(count.keys())
    names_new.sort()
    
    print()
    print("Vote counts:")
    #formating
    for i in names_new:
        print('{0:<10}'.format(i),"-",count[i])
    
        
        
electrol_commission()        