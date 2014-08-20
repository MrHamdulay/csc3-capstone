#question 2

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

#yes=True
#no=False

firstq=input("Did anyone see you? (yes/no)\n")

while firstq=="yes": 
        
        sq=input("Was it a boss/lover/parent? (yes/no)\n")
        
        if sq=="no":
                
                print("Decision: Eat it.")
                
                firstq="lastq"
                
        if sq=="yes":
                
                tq=input("Was it expensive? (yes/no)\n")
                
                if tq=="no":
                        
                        fq=input("Is it chocolate? (yes/no)\n")
                        
                        if fq=="yes":
                                
                                print("Decision: Eat it.")
                                firstq="lastq"
                                
                        else:
                                
                                print("Decision: Don't eat it.")
                                firstq="lastq"
                                
                if tq=="yes":
                        
                        fifq=input("Can you cut off the part that touched the floor? (yes/no)\n")
                        
                        if fifq=="no":
                                
                                print("Decision: Your call.")
                                firstq="lastq"
                                
                        else:
                                print("Decision: Eat it.")
                                firstq="lastq"
                                
while firstq=="no":
        
        oo=input("Was it sticky? (yes/no)\n")
        
        if oo=="no":
                
                mq=input("Is it an Emausaurus? (yes/no)\n")
               
                if mq=="yes":
                        
                        nq=input("Are you a Megalosaurus? (yes/no)\n")
                        if nq=="no":
                                
                                print("Decision: Don't eat it.")
                                firstq="lastq"
                                
                        if nq=="yes":
                                
                                print("Decision: Eat it.")
                                firstq="lastq"
                                
                if mq=="no":
                        
                        oq=input("Did the cat lick it? (yes/no)\n")
                        if oq=="yes":
                                
                                pq=input("Is your cat healthy? (yes/no)\n")
                                
                                if pq=="yes":
                                        
                                        print("Decision: Eat it.")
                                        firstq="lastq"
                                        
                                if pq=="no":
                                        
                                        print("Decision: Your call.")
                                        firstq="lastq"
                                        
                        if oq=="no":
                                
                                print("Decision: Eat it.")
                                firstq="lastq"
                                
        if oo=="yes":
                
                rq=input("Is it a raw steak? (yes/no)\n")
                if rq=="yes":
                        
                        sq=input("Are you a puma? (yes/no)\n")
                        
                        if sq=="no":
                                
                                print("Decision: Don't eat it.")
                                firstq="lastq"
                                
                        if sq=="yes":
                                
                                print("Decision: Eat it.")
                                firstq="lastq"
                                
                if rq=="no":
                        
                        tq=input("Did the cat lick it? (yes/no)\n")
                        if tq=="no":
                                
                                print("Decision: Eat it.")
                                firstq="lastq"
                                
                        if tq=="yes":
                                
                                uq=input("Is your cat healthy? (yes/no)\n")
                                
                                if uq=="yes":
                                        
                                        print("Decision: Eat it.")
                                        firstq="lastq"
                                        
                                if uq=="no":
                                        
                                        print("Decison: Your call.")
                                        firstq="lastq"
                                
                                
                       
                       

