print('''Welcome to the 30 Second Rule Expert
------------------------------------ 
Answer the following questions by selecting from among the options.''')
text = ""
    
def question(index):
    if index == 0:
        text = "Did anyone see you? (yes/no)\n"
        if (input(text) == "yes"):
            question(8)
        else:
            question(1)
    if index == 1:
        text = "Was it sticky? (yes/no)\n"
        if (input(text) == "yes"):
            question(4)
        else:
            question(2)
    if index == 2:
        text = "Is it an Emausaurus? (yes/no)\n"
        if (input(text) == "yes"):
            question(3)
        else:
            question(5)    
    if index == 3:
        text = "Are you a Megalosaurus? (yes/no)\n"
        if (input(text) == "yes"):
            question(12)
        else:
            question(13)  
    if index == 4:
        text = "Is it a raw steak? (yes/no)\n"
        if (input(text) == "yes"):
            question(7)
        else:
            question(5) 
    if index == 5:
        text = "Did the cat lick it? (yes/no)\n"
        if (input(text) == "yes"):
            question(6)
        else:
            question(12)
    if index == 6:
        text = "Is your cat healthy? (yes/no)\n"
        if (input(text) == "yes"):
            question(12)
        else:
            question(14)        
    if index == 7:
        text = "Are you a puma? (yes/no)\n"
        if (input(text) == "yes"):
            question(12)
        else:
            question(13)   
    if index == 8:
        text = "Was it a boss/lover/parent? (yes/no)\n"
        if (input(text) == "yes"):
            question(9)
        else:
            question(12)  
    if index == 9:
        text = "Was it expensive? (yes/no)\n"
        if (input(text) == "yes"):
            question(11)
        else:
            question(10)  
    if index == 10:
        text = "Is it chocolate? (yes/no)\n"
        if (input(text) == "yes"):
            question(12)
        else:
            question(13)  
    if index == 11:
        text = "Can you cut off the part that touched the floor? (yes/no)\n"
        if (input(text) == "yes"):
            question(12)
        else:
            question(14)
    if index == 12:
        print("Decision: Eat it.")
    if index == 13:
        print("Decision: Don't eat it.")
    if index == 14:
        print("Decision: Your call.")
        
question(0)