print("Welcome to the 30 Second Rule Expert\n"+36*"-"+"\nAnswer the following questions by selecting from among the options.")
opening_quiz = input("Did anyone see you? (yes/no)\n")

if opening_quiz.lower() == "yes":
    who_saw = input("Was it a boss/lover/parent? (yes/no)\n")
    
    if who_saw.lower() == "yes":
        was_it_expensive = input("Was it expensive? (yes/no)\n")
        if was_it_expensive.lower() == "yes":
            
            can_you_cut = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if can_you_cut.lower() == "yes":
                print("Decision: Eat it.")
            elif can_you_cut.lower() == "no":
                print("Decision: Your call.")
                
        elif was_it_expensive.lower() == "no":
            is_it_chocolate = input("Is it chocolate? (yes/no)\n")
            if is_it_chocolate.lower() == "yes":
                print("Decision: Eat it.")
            elif is_it_chocolate.lower() == "no":
                print("Decision: Don't eat it.")
                
    elif who_saw.lower() == "no":
        print("Decision: Eat it.")
            
elif opening_quiz.lower() == "no":
    was_it_sticky = input("Was it sticky? (yes/no)\n")
    if was_it_sticky.lower() == "yes":
        is_it_a_raw_steak = input("Is it a raw steak? (yes/no)\n")
        if is_it_a_raw_steak.lower() == "yes":
            are_you_a_puma = input("Are you a puma? (yes/no)\n")
            if are_you_a_puma.lower() == "yes":
                print("Decision: Eat it.")
            elif are_you_a_puma.lower() == "no":
                print("Decision: Don't eat it.")
                
        elif is_it_a_raw_steak.lower() == "no":
            did_the_cat_lick_it = input("Did the cat lick it? (yes/no)\n")
            if did_the_cat_lick_it.lower() == "yes":
                is_your_cat_healthy = input("Is your cat healthy? (yes/no)\n")
                if is_your_cat_healthy.lower() == "yes":
                    print("Decision: Eat it.")
                elif is_your_cat_healthy.lower() == "no":
                    print("Decision: Your call.")
            elif did_the_cat_lick_it.lower() == "no":
                print("Decision: Eat it.")
                
    elif was_it_sticky.lower() == "no":
        is_it_an_emausaurus = input("Is it an Emausaurus? (yes/no)\n")
        if is_it_an_emausaurus == "yes":
            are_you_a_megalosaurus = input("Are you a Megalosaurus? (yes/no)\n")
            if are_you_a_megalosaurus.lower() == "yes":
                print("Decision: Eat it.")
            elif are_you_a_megalosaurus.lower() == "no":
                print("Decision: Don't eat it.")
                
        elif is_it_an_emausaurus == "no":
            did_the_cat_lick_it = input("Did the cat lick it? (yes/no)\n")
            if did_the_cat_lick_it.lower() == "yes":
                is_your_cat_healthy = input("Is your cat healthy? (yes/no)\n")
                if is_your_cat_healthy.lower() == "yes":
                    print("Decision: Eat it.")
                elif is_your_cat_healthy.lower() == "no":
                    print("Decision: Your call.")
            elif did_the_cat_lick_it.lower() == "no":
                print("Decision: Eat it.")            