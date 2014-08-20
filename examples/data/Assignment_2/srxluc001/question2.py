#program to on whether to make a decision or not
#Lucy Sure
#SRXLUC001
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

x=input("Did anyone see you? (yes/no)\n")
if(x=="yes"):
    a=input("Was it a boss/lover/parent? (yes/no)\n")
    if (a=="yes"):
        b=input("Was it expensive? (yes/no)\n")
        if(b=="yes"):
            d=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (d=="yes"):
                    print("Decision: Eat it.")
            else:
                    print("Decision: Your call.")
        if(b=="no"):
            c=input("Is it chocolate? (yes/no)\n")
            if(c=="yes"):
                print("Decision: Eat it.")
            if(c=="no"):
                print("Decision: Don't eat it.")
    if(a=="no"):
            print("Decision: Eat it.")
else:
    if(x=="no"):
        e=input("Was it sticky? (yes/no)\n")
        if(e=="no"): 
            f=input("Is it an Emausaurus? (yes/no)\n")
            if(f=="yes"):
                g=input("Are you a Megalosaurus? (yes/no)\n")
                if(g=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")   
                    if(f=="no"):
                        u=input("Did the cat lick it?(yes/no)\n")
                        if(u=="yes"):
                            j=input("Is your cat healthy?(yes/no)\n")
                            if(j=="yes"):
                                    print("Decision: Eat it.")
                            else:
                                if(j=="no"):
                                            print("Decision: Your call.")          
        if(e=="yes"):
                h=input("Is it a raw steak? (yes/no)\n")
                if(h=="no"):
                    u=input("Did the cat lick it? (yes/no)\n")
                    if(u=="no"):
                            print("Decision: Eat it.")
                    if(u=="yes"):
                        j=input("Is your cat healthy? (yes/no)\n")
                        if(j=="yes"):
                            print("Decision: Eat it.")
                        else:
                            print("Decision: Your call.")
                if(h=="yes"):
                    i=input("Are you a puma? (yes/no)\n")
                    if(i=="yes"):
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Don't eat it.")
                        
                
              
                  
                     
            














