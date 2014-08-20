print("Welcome to the 30 Second Rule Expert") 
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
firstq=input("Did anyone see you? (yes/no) \n")
if (firstq=='yes'):
    secondq=input("Was it a boss/lover/parent? (yes/no) \n")
    if(secondq=='yes'):
        thirdq=input("Was it expensive? (yes/no)\n")
        if(thirdq=='yes'):
            fourthq=input("Can you cut off the part that touched the floor? (yes/no) \n")
            if (fourthq=='yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            fifthq=input("Is it chocolate? (yes/no) \n")
            if(fifthq=='yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
        
else:
    secondq1=input("Was it sticky? (yes/no) \n")
    if(secondq1=='yes'):
        thirdq1=input("Is it a raw steak? (yes/no) \n")
        if(thirdq1=='yes'):
            fifthq1=input("Are you a puma? (yes/no) \n")
            if(fifthq1=='yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            sixthq1= input("Did the cat lick it? (yes/no) \n")
            if(sixthq1=='yes'):
                ninthq1=input("Is your cat healthy? (yes/no) \n")
                if(ninthq1=='yes'):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
                
    else:
        fourthq1=input("Is it an Emausaurus? (yes/no) \n")
        if (fourthq1=='yes'):
            seventhq1=input("Are you a Megalosaurus? (yes/no) \n")
            if (seventhq1=='yes'):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            eighthq1=input("Did the cat lick it? (yes/no) \n")
            if(eighthq1=='yes'):
                tenthq1=input("Is your cat healthy? (yes/no) \n")
                if(tenthq1=='yes'):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
                
            
        
    
    
