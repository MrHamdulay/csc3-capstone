#30 second expert
#Siphesihle Cele
#17 march 2014

print("Welcome to the 30 Second Rule Expert")   #Introduction printed
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

think=input("Did anyone see you? (yes/no)\n")            #decision tree for the computer to move around, determined by the users input
if think =='yes':
    action1=input("Was it a boss/lover/parent? (yes/no)\n")
    if action1=='no':
        print("Decision: Eat it.")
    else:
        action2=input("Was it expensive? (yes/no)\n")  #else condition that comes to action if first condition is not met.
        if action2=='yes':
            action2_1=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if action2_1=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            action2_2=input("Is it chocolate? (yes/no)\n")
            if action2_2=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
else:
    action3= input("Was it sticky? (yes/no)\n")      #determines the stickyness of the good.
    if action3=='yes':
        action3_1=input("Is it a raw steak? (yes/no)\n")
        if action3_1=='yes':
            action4= input("Are you a puma? (yes/no)\n")
            if action4=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            action5=input("Did the cat lick it? (yes/no)\n")
            if action5=='no':
                print("Decision: Eat it.")
            else:
                action5_2=input("Is your cat healthy? (yes/no)\n")
                if action5_2=='no':
                    print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
    else:
        action6=input("Is it an Emausaurus? (yes/no)\n")
        if action6=='yes':
            action6_2=input("Are you a Megalosaurus? (yes/no)\n")
            if action6_2=='yes':
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            action6_3=input("Did the cat lick it? (yes/no)\n")
            if action6_3=='yes':
                action7=input("Is your cat healthy? (yes/no)\n")
                if action7=='yes':
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
                