#program to discover whether or not to eat dropped food
#vuyolwethu nkosi
#8 march 2014

print("Welcome to the 30 Second Rule Expert")
print("-"*36)
print("Answer the following questions by selecting from among the options.")
x=input("Did anyone see you? (yes/no)\n")
if(x=="yes"):
    boss_lover_parent=input("Was it a boss/lover/parent? (yes/no)\n")
    if(boss_lover_parent=="yes"):
        expensive=input("Was it expensive? (yes/no)\n")
        if(expensive=="yes"):
            touch_floor=input("Can you cut off the part that touched the floor? (yes/no)\n")
            if(touch_floor=="yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            chocolate=input("Is it chocolate? (yes/no)\n")
            if(chocolate=="yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    sticky=input("Was it sticky? (yes/no)\n")
    if(sticky=="yes"):
        raw_steak=input("Is it a raw steak? (yes/no)\n")
        if(raw_steak=="yes"):
            puma=input("Are you a puma? (yes/no)\n")
            if(puma=="yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat_lick=input("Did the cat lick it? (yes/no)\n")
            if(cat_lick=="yes"):
                healthy_cat=input("Is your cat healthy? (yes/no)\n")
                if(healthy_cat=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        emausaurus=input("Is it an Emausaurus? (yes/no)\n")
        if(emausaurus=="yes"):
            megalosaurus=input("Are you a Megalosaurus? (yes/no)\n")
            if(megalosaurus=="yes"):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat_lick=input("Did the cat lick it? (yes/no)\n")
            if(cat_lick=="yes"):
                healthy_cat=input("Is your cat healthy? (yes/no)\n")
                if(healthy_cat=="yes"):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")        
        
        
            

            
    