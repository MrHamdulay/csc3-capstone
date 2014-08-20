def rightAligned(x,y):
    print("")
    print("Right-aligned list:")
    for i in range(len(x)):
        l = y-len(x[i])
        print(" "*l,x[i],sep="")

def getWords():
    user = input("Enter strings (end with DONE):\n")
    list = []
    length = len(user)
    while user.lower() != "done": 
        list.append(user)
        user = input("")
        if len(user) > length:
            length = len(user)
    rightAligned(list,length) 
getWords()    
            

        
    
    

    