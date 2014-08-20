print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
question1=input("Did anyone see you? (yes/no)\n")
if(question1=="yes"):
    question2=input("Was it a boss/lover/parent? (yes/no)\n")
    if(question2=="no"):
        print("Decision: Eat it.")
    if(question2=="yes"):
        question3=input("Was it expensive? (yes/no)\n")    
        if(question3=="yes"):
            question4=input("Can you cut off the part that touched the floor? (yes/no)\n")  
            if(question4=="yes"):
                print("Decision: Eat it.") 
            if(question4=="no"):
                print("Decision: Your call.")
        if(question3=="no"):
            question5=input("Is it chocolate? (yes/no)\n")
            if(question5=="yes"):
                print("Decision: Eat it.")
            if(question5=="no"):
                print("Decision: Don't eat it.")
if(question1=="no"):
    question6=input("Was it sticky? (yes/no)\n")
    if(question6=="yes"):
        question9=input("Is it a raw steak? (yes/no)\n")
        if(question9=="yes"):
            question10=input("Are you a puma? (yes/no)\n")
            if(question10=="yes"):
                print("Decision: Eat it.")
            if(question10=="no"):
                print("Decision: Don't eat it.")
        if(question9=="no"):
            question11=input("Did the cat lick it? (yes/no)\n")
            if(question11=="no"):
                print("Decision: Eat it.")
            if(question11=="yes"):
                question12=input("Is your cat healthy? (yes/no)\n")
                if(question12=="yes"):
                    print("Decision: Eat it.")
                if(question12=="no"):
                    print("Decision: Your call.")
    if(question6=="no"):
        question13=input("Is it an Emausaurus? (yes/no)\n")
        if(question13=="no"):
            question11=input("Did the cat lick it? (yes/no)\n")
            if(question11=="no"):
                print("Decision: Eat it.")
            if(question11=="yes"):
                question12=input("Is your cat healthy? (yes/no)\n")
                if(question12=="yes"):
                    print("Decision: Eat it.")
                if(question12=="no"):
                        print("Decision: Your call.")  
        if(question13=="yes"):
            question14=input("Are you a Megalosaurus? (yes/no)\n")
            if(question14=="no"):
                print("Decision: Don't eat it.")
            if(question14=="yes"):
                print("Decision: Eat it.")
                 

   
    
    
    


