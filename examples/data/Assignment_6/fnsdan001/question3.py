parties = []
votes =[]
print("Independent Electoral Commission")
print("--------------------------------")
string = input("Enter the names of parties (terminated by DONE):\n")
if string!="DONE":
    votes.append( 1)
    parties.append(string)
    cnt = 1
    index = 0
    done = 0
    i = 1
    run = 0
    out = []
    while string!= "DONE":
        string = input()
        if string == "DONE":
            
            break
    
    

        elif string not in parties:
            parties.append(string)
            votes.append( 1)
            i+=1
        else:
            index = parties.index(string)
            votes[index]+=1
              

  

    for i in range(len(parties)):
        out.append(parties[i] +'0'+ str(votes[i]))

    outa = sorted(out)
    print()
    print("Vote counts:")

    for i in parties:
        print('{:<10}'.format(outa[run].split("0",1)[0]) + ' - ' + str(outa[run].split("0",1)[1]))
        run+=1
        
else:
    
    print()
    print("Vote counts:")
    
    
    
