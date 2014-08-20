# checking whether food should be eaten or not
#Karabo Choma
# March 14

def food():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
    a=input("Did anyone see you? (yes/no)" '\n')
    if (a=='yes'):
        b=input("Was it a boss/lover/parent? (yes/no)" '\n')
        if (b=='yes'):
            c=input("Was it expensive? (yes/no)" '\n')
            if (c=='yes'):
                e=input("Can you cut off the part that touched the floor? (yes/no)" '\n')
                if (e=='yes'):
                    print("Decision: Eat it.")
                if (e=='no'):
                        print("Decision: Your call.")
            if (c=='no'):
                d=input("Is it chocolate? (yes/no)" '\n')
                if(d=='yes'):
                    print("Decision: Eat it.")
                if (d=='no'):
                    print("Decision: Don't eat it.")                
        if (b=='no'):
            print("Decision: Eat it.")
    if (a=='no'):
        f=input("Was it sticky? (yes/no)" '\n')
        if (f=='yes'):
            h=input("Is it a raw steak? (yes/no)" '\n')
            if (h=='yes'):
                k=input("Are you a puma? (yes/no)" '\n')
                if (k=='yes'):
                    print("Decision: Eat it.")
                if (k=='no'):
                    print("Decision: Don't eat it.")
            if (h=='no'):
                j=input("Did the cat lick it? (yes/no)" '\n')
                if (j=='yes'):
                    l=input("Is your cat healthy? (yes/no)" '\n')
                    if (l=='yes'):
                        print("Decision: Eat it.")
                    if (l=='no'):
                        print("Decision: Your call.")
                if (j=='no'):
                    print("Decision: Eat it.")
        if (f=='no'):
            g=input("Is it an Emausaurus? (yes/no)" '\n')
            if (g=='yes'):
                i=input("Are you a Megalosaurus? (yes/no)" '\n')
                if (i=='yes'):
                    print("Decision: Eat it.")
                if (i=='no'):
                    print("Decision: Don't eat it.")
            if (g=='no'):
                j=input("Did the cat lick it? (yes/no)" '\n')
                if (j=='yes'):
                    l=input("Is your cat healthy? (yes/no)" '\n')
                    if (l=='yes'):
                        print("Decision: Eat it.")
                    if (l=='no'):
                            print("Decision: Your call.")
                if (j=='no'):
                    print("Decision: Eat it.")                
                
            
                
                
   
      
                
food()
                