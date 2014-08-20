#shahrain Coovadia
#CVDSHA002

def list():
    sum=[]                                                      #empty string   
    print("Enter the names of parties (terminated by DONE):")   #ask for inputs
    string=input()
    if string!= "DONE":
        sum.append(string)        #add string
        while sum:
            string=input()
            if string=="DONE":
                break
            sum.append(string)       #add string
    return sum

def votes():                  #define new function
    print("Independent Electoral Commission")
    print("--------------------------------")
    add=list()                        
    new=[]                     #empty string
    for i in add:
        if i in new:
            continue
        new.append(i)      #add on 
    new=sorted(new)
    print("\nVote counts:")
    
    for t in new:
        print(t.ljust(10), "-", add.count(t),)    #adjust spacing
        
votes()