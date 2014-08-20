""" List of names
Tameryn Pillay
20 April """

def names():
    
    # get the names
    
    answer = input ("Enter strings (end with DONE):\n")
    names = []
    while answer != "DONE":
        names.append(answer)
        answer= input()
    print()
    
    # finding max length from list of names
    
    max_length = names[0]
    for i in range(len(names)):
        if len(names[i]) > len(max_length):
            max_length = names[i]
    y = (max_length) # set max length of word equal to y   
            
    # formatting to get required output
    
    print("Right-aligned list:")
    for name in names:
        p = str(len(y))
        h = "{0:>"+p+"}"
        print(h.format(name))
        
       
names()