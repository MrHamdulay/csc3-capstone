#program for determining if one should eat a cupcake
# by Karidas Tshintsholo

print( "Welcome to the 30 Second Rule Expert")
print( "------------------------------------")
print ("Answer the following questions by selecting from among the options.")
FirstQ=input("Did anyone see you? (yes/no) \n")
# Right hand side of the diagram
if FirstQ=="yes":
    SecondQ=input("Was it a boss/lover/parent? (yes/no) \n")
    if SecondQ=="no":
        print ("Decision: Eat it.")
# The "Was it expensive" interchange.
    elif SecondQ=="yes":
        ThirdQ=input("Was it expensive? (yes/no) \n")
        if ThirdQ=="yes":
            FourthQ=input("Can you cut off the part that touched the floor? (yes/no) \n")
            if FourthQ=="yes":
                print("Decision: Eat it.")
            elif FourthQ=="no":
                print ("Decision: Your call.")
        elif ThirdQ=="no":
            FifthQ=input("Is it chocolate? (yes/no) \n")
            if FifthQ=="yes":
                print ("Decision: Eat it.")
            elif FifthQ=="no":
                print ("Decision: Don't eat it.")
#Left handside of the diagram.

elif FirstQ=="no":
    Q1=input("Was it sticky? (yes/no) \n")
# Main interchange on the left hand side of the diagram. "Was it sticky? (right)".

    if Q1=="yes":
# The STAKE interchange.
        
        Q2=input("Is it a raw steak? (yes/no) \n")
        if Q2=="yes":
            Z=input("Are you a puma? (yes/no) \n")
            if Z=="yes":
                print("Decision: Eat it.")
            elif Z=="no":
                print ("Decision: Don't eat it.")
        elif Q2=="no":
# Checking IF THE CAT LICKED IT
            
            Q3=input("Did the cat lick it? (yes/no) \n")
            if Q3=="no":
                print ("Decision: Eat it.")
            elif Q3=="yes":
                Q4=input("Is your cat healthy? (yes/no) \n")
                if Q4=="yes":
                    print ("Decision: Eat it.")
                elif Q4=="no":
                    print ("Decision: Your call.")
    elif Q1=="no":
# Dinasour bridge
        Q5=input ("Is it an Emausaurus? (yes/no) \n")
        if Q5=="yes":
            Q6=input ("Are you a Megalosaurus? (yes/no) \n")
            if Q6=="yes":
                print ("Decision: Eat it.")
            elif Q6=="no":
                print ("Decision: Don't eat it.")
        elif Q5=="no":
            Q6=input("Did the cat lick it? (yes/no) \n")
            if Q6=="no":
                print ("Decision: Eat it.")
            elif Q6=="yes":
                Q7=input("Is your cat healthy? (yes/no) \n")
                if Q7=="yes":
                    print ("Decision: Eat it.")
                elif Q7=="no":
                    print ("Decision: Your call.")
            
            