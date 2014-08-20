#artificial intelligence
print("Welcome to the 30 Second Rule Expert")
print("-" * 36)
print("Answer the following questions by selecting from among the options.")

        
def no():
    
    y=input("Was it sticky? (yes/no)\n")
    
    if(y=="yes"):
                x=input("Is it a raw steak? (yes/no)\n")
                if(x=="yes"):
                    r=input("Are you a puma? (yes/no)\n")
                    if(r=="yes"):
                        print("Decision: Eat it.")
                    if(r=="no"):
                        print("Decision: Don't eat it.")
                    
                if(x=="no"):
                    z=input("Did the cat lick it? (yes/no)\n")
                    if(z=="yes"):
                        w=input("Is your cat healthy? (yes/no)\n")
                        if(w=="no"):
                            print("Decision: Your call.")
                        if(w=="yes"):
                            print("Decision: Eat it.")
                            
                    if(z=="no"):
                        print("Decision: Eat it.")
                    
                    
    if(y=="no"):
        b=input("Is it an Emausaurus? (yes/no)\n")
        if(b=="no"):
            c=input("Did the cat lick it? (yes/no)\n")
            if(c=="yes"):
                d=input("Is your cat healthy? (yes/no)\n")
                if(d=="yes"):
                    print("Decision: Eat it.")
                if(d=="no"):
                    print("Decision: Your call.")
            if(c=="no"):
                print("Decision: Eat it.")
                
        if(b=="yes"):
            a=input("Are you a Megalosaurus? (yes/no)\n")
            if(a=="yes"):
                print("Decision: Eat it.")
            if(a=="no"):
                print("Decision: Don't eat it.")
             
                
                
        
                
                
def yes():
    e=input("Was it a boss/lover/parent? (yes/no)\n")
    if(e=="yes"):
        f=input("Was it expensive? (yes/no)\n")
        if(f=="yes"):
            g=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(g=="yes"):
                print("Decision: Eat it.")
            if(g=="no"):
                print("Decision: Your call.")
        if(f=="no"):
            h=input("Is it chocolate? (yes/no)\n")
            if(h=="yes"):
                print("Decision: Eat it.")
            if(h=="no"):
                print("Decision: Don't eat it.")
    if(e=="no"):
        print("Decision: Eat it.")
            
                     
x=input("Did anyone see you? (yes/no)\n")
if(x=="yes"):
    yes()
            
if(x=="no"):
    no()    
        
        


        
















        
                
                
            
        
        

    

    
      
           
        
         
    

    

            
