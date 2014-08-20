#Opening print lines
print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

#Start of flow chart
answ = input("Did anyone see you? (yes/no)\n")
if (answ=="yes"):
    answ = input("Was it a boss/lover/parent? (yes/no)\n")
    if (answ=="yes"):
        answ = input("Was it expensive? (yes/no)\n")
        if (answ=="yes"):
            answ = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if (answ=="yes"):
                print("Decision: Eat it.")#end   
            else:
                print("Decision: Your call.")#end
        else:
            answ = input("Is it chocolate? (yes/no)\n")
            if(answ=="yes"):
                print("Decision: Eat it.")#end
            else:
                print("Decision: Don't eat it.")#end
            
    else:
        print("Decision: Eat it.")#end
        
else:
    answ = input("Was it sticky? (yes/no)\n")
    if (answ=="yes"):
        answSteak = input("Is it a raw steak? (yes/no)\n")
        if (answSteak=="yes"):
            answ = input("Are you a puma? (yes/no)\n")
            if (answ=="yes"):
                print("Decision: Eat it.")#end
            else:
                print("Decision: Don't eat it.")#end
        else:
            answ = input("Did the cat lick it? (yes/no)\n")
            if (answ=='yes'):
                answ = input("Is your cat healthy? (yes/no)\n")
                if (answ=='yes'):
                    print("Decision: Eat it.")#end
                else:
                    print("Decision: Your call.")#end
            else:
                print("Decision: at it.")#end
    else:
        answ = input("Is it an Emausaurus? (yes/no)\n")
        if (answ=='yes'):
            answ = input("Are you a Megalosaurus? (yes/no)\n")
            if (answ=='yes'):
                print("Decision: Eat it.")#end
            else:
                print("Decision: Don't eat it.")#end
        else:
            answ = input("Did the cat lick it? (yes/no)\n")
            if (answ=='yes'):
                answ = input("Is your cat healthy? (yes/no)\n")
                if (answ=='yes'):
                    print("Decision: Eat it.")#end
                else:
                    print("Decision: Your call.")#end 
            else:
                print("Decision: Eat it.")#end
        