#Assignment 2
#Question 2
#Flowchart of whether  or not you should eat the food

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
m=input("Did anyone see you? (yes/no)\n")
if m=="yes":
    s=input("Was it a boss/lover/parent? (yes/no)\n")
    if s=="yes":
        x=input("Was it expensive? (yes/no)\n")
        if x=="yes":
            y=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if y=="yes":
                print("Decision: Eat it.")
            if y=="no":
                print("Decision: Your call.")
        if x=="no":
            z=input("Is it chocolate? (yes/no)\n")
            if z=="yes":
                print("Decision: Eat it.")
            if z=="no":
                print("Decision: Don't eat it.")
    if s=="no":
        print("Decision: Eat it.")
        
if m=="no":
    n=input("Was it sticky? (yes/no)\n")
    if n=="yes":
        x=input("Is it a raw steak? (yes/no)\n")
        if x=="yes":
            y=input("Are you a puma? (yes/no)\n")
            if y=="yes":
                print("Decision: Eat it.")
            if y=="no":
                print("Decision: Don't eat it.")
        if x=="no":
            y=input("Did the cat lick it? (yes/no)\n")
            if y=="yes":
                x=input("Is your cat healthy? (yes/no)\n")
                if x=="yes":
                    print("Decision: Eat it.")
                if x=="no":
                    print("Decision: Your call.")
            if y=="no":
                print("Decision: Eat it.")
    if n=="no":
        x=input("Is it an Emausaurus? (yes/no)\n")
        if x=="yes":
            y=input("Are you a Megalosaurus? (yes/no)\n")
            if y=="yes":
                print("Decision: Eat it.")
            if y=="no":
                print("Decision: Don't eat it.")
        if x=="no":
            y=input("Did the cat lick it? (yes/no)\n")
            if y=="yes":
                x=input("Is your cat healthy? (yes/no)\n")
                if x=="yes":
                    print("Decision: Eat it.")
                if x=="no":
                    print("Decision: Your call.")
            if y=="no":
                print("Decision: Eat it.")            
                         
            
        