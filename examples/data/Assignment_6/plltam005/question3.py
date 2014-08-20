""" Elections
Tameryn Pillay
23 April """


def elections():
    print("Independent Electoral Commission")
    print("--------------------------------")
    
    # get votes
    answer = input ("Enter the names of parties (terminated by DONE):\n")
    names = []
    while answer != "DONE":
        names.append(answer)
        answer= input()
    print()  
    
    # counting the votes
    counter = {}
    
    # count words and add new words as they are encountered
    for name in names:
        if not name in counter:
            counter[name] = 1
        else:
            counter[name] += 1
            
    # print out results        
    print("Vote counts:")
    for name in counter:
        print("{0:<10}".format(name)," - ",counter[name],sep='')
    

        
    
elections()