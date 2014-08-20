#Student Number: GPXSHI001
#FOOOOOOOOOOD!
#12/03/2014

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

answer=""
answer=input("Did anyone see you? (yes/no)\n")

if(answer=="yes"):
    answer=input("Was it a boss/lover/parent? (yes/no)\n")
    if(answer=="yes"):
        answer=input("Was it expensive? (yes/no)\n")
        if(answer=="yes"):
            answer=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(answer=="yes"):
                print("Decision: Eat it.")
            else: print("Decision: Your call.")
        else:
            answer=input("Is it chocolate? (yes/no)\n")
            if(answer=="no"): print("Decision: Don't eat it.")
            else: print("Decision: Eat it.")
    else: print("Decision: Eat it.")
else:
    answer=input("Was it sticky? (yes/no)\n")
    if(answer=="yes"):
        answer=input("Is it a raw steak? (yes/no)\n")
        
        if(answer=="yes"):
            answer=input("Are you a puma? (yes/no)\n")
            
            if(answer=="yes"):
                print("Decision: Eat it.")
                
            else: print("Decision: Don't eat it.")
        else:
            answer=input("Did the cat lick it? (yes/no)\n")
            if(answer=="yes"):
                answer=input("Is your cat healthy? (yes/no)\n")
                if(answer=="yes"):
                    print("Decision: Eat it.")
                else: print("Decision: Your call.")
            else: print("Decision: Eat it.")
            
    else:
        answer=input("Is it an Emausaurus? (yes/no)\n")
        if(answer=="yes"):
            answer=input("Are you a Megalosaurus? (yes/no)\n")
            
            if(answer=="yes"): print("Decision: Eat it.")
            else: print("Decision: Don't eat it.")
        else:
            answer=input("Did the cat lick it? (yes/no)\n")
            if(answer=="yes"):
                answer=input("Is your cat healthy? (yes/no)\n")
                if(answer=="yes"): print("Decision: Eat it.")
                else: print("Decision: Your call.")
            else: print("Decision: Eat it.")            