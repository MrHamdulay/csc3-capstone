print ("Welcome to the 30 Second Rule Expert")
print ("------------------------------------")
print ("Answer the following questions by selecting from among the options.")
ans1 = input("Did anyone see you? (yes/no)\n")
if ans1 == 'yes':
    ans2 = input("Was it a boss/lover/parent? (yes/no)\n")
    if ans2 == 'yes':
        ans3 = input("Was it expensive? (yes/no)\n")
        if ans3 == 'yes':
            ans4 = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if ans4 == 'no':
                print ("Decision: Your call.")
            elif ans4 == 'yes':
                print("Decision: Eat it.")
            
        if ans3 == 'no':
            ansChoc = input("Is it chocolate? (yes/no)\n")
            if ansChoc == 'yes':
                print ("Decision: Eat it.")
            elif (ansChoc == 'no'):
                print ("Decision: Don't eat it.")   
   
   
    elif ans2 == 'no':
        print("Decision: Eat it.")
        
                

elif ans1 == 'no':
    ans2 = input ("Was it sticky? (yes/no)\n")
    if ans2 == 'yes':
        ans3 = input("Is it a raw steak? (yes/no)\n")
        if ans3 == 'yes':
            ans4 = input ("Are you a puma? (yes/no)\n")
            if ans4 == 'yes':
                print("Decision: Eat it.")
            elif ans4 == 'no':
                print("Decision: Don't eat it.")
        elif ans3 == 'no':
            ans4 = input("Did the cat lick it? (yes/no)\n")
            if ans4 == 'no':
                print ("Decision: Eat it.")
            elif ans4 == 'yes':
                ans5 = input("Is your cat healthy? (yes/no)\n")
                if ans5 == 'yes':
                    print ("Decision: Eat it.")
                elif ans5 == 'no':
                    print ("Decision: Your call.")
                                
                                
    elif ans2 == 'no':
        ans3 = input("Is it an Emausaurus? (yes/no)\n")
        if ans3 == 'yes':
            ans4 = input("Are you a Megalosaurus? (yes/no)\n")
            if ans4 == 'yes':
                print ("Decision: Eat it.")
            elif ans4 == 'no':
                print ("Decision: Don't eat it.")
        elif ans3 == 'no':
            ans4 = input("Did the cat lick it? (yes/no)\n")
            if ans4 == 'no':
                print ("Decision: Eat it.")
            elif ans4 == 'yes':
                ans5 = input("Is your cat healthy? (yes/no)\n")
                if ans5 == 'yes':
                    print ("Decision: Eat it.")
                elif ans5 == 'no':
                    print ("Decision: Your call.")            
            
                            
                            
#Welcome to the 30 Second Rule Expert
#------------------------------------
#Answer the following questions by selecting from among the options.
#Did anyone see you? (yes/no)
#yes
#Was it a boss/lover/parent? (yes/no)
#yes
#Was it expensive? (yes/no)
#yes
#Can you cut off the part that touched the floor? (yes/no)
#no
#Decision: Your call.