print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")



def qright():
    person = input("Was it a boss/lover/parent? (yes/no) \n")
    if person == "no":
        print("Decision: Eat it.")
    else:
        price = input("Was it expensive? (yes/no) \n")
        if price == "yes":
            floor = input("Can you cut off the part that touched the floor? (yes/no) \n")
            if floor == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
                
        else:
            chocolate = input("Is it chocolate? (yes/no) \n")
            if chocolate == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
                
                
                
def cat():
    cat = input("Did the cat lick it? (yes/no) \n")
    if cat == "no":
        print("Decision: Eat it.")
    else:
        healthy = input("Is your cat healthy? (yes/no) \n")
        if healthy == "yes":
            print("Decision: Eat it.")
        else:
            print("Decision: Your call.")
    
    

def qleft():
    sticky = input("Was it sticky? (yes/no) \n")
    if sticky == "yes":
        raw_steak = input("Is it a raw steak? (yes/no) \n")
        if raw_steak == "yes":
            puma = input("Are you a puma? (yes/no) \n")
            if puma == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat()



    
    else:
        Emausaurus = input("Is it an Emausaurus? (yes/no) \n")
        if Emausaurus == "no":
            cat()
            
        else:
            Megalosaurus = input("Are you a Megalosaurus? (yes/no) \n")
            if Megalosaurus == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
            










first_answer = input("Did anyone see you? (yes/no) \n")

if first_answer == "yes":
    qright()
elif first_answer == "no":
    qleft()
    
