def displayName():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    
def main():
    Ei="Decision: Eat it."
    Dne="Decision: Don't eat it."
    Yc="Decision: Your call."
    see=input("Did anyone see you? (yes/no) \n")
    if see == "yes":
        peer=input("Was it a boss/lover/parent? (yes/no) \n")
        if peer=="yes":
            ex=input("Was it expensive? (yes/no) \n")
            if ex=="yes":
                part=input("Can you cut off the part that touched the floor? (yes/no) \n")
                if part=="yes":
                    print(Ei)
                elif part=="no":
                    print(Yc)
            elif ex=="no":
                choc=input("Is it chocolate? (yes/no) \n")
                if choc=="yes":
                    print(Ei)
                elif choc=="no":
                    print(Dne)
        elif peer=="no":
            print(Ei)
    elif see=="no":
        st=input("Was it sticky? (yes/no) \n")
        if st=="yes":
            rs=input("Is it a raw steak? (yes/no) \n")
            if rs== "yes":
                puma=input("Are you a puma? (yes/no) \n")
                if puma=="yes":
                    print(Ei)
                elif puma=="no":
                    print(Dne)
            elif rs=="no":
                cat=input("Did the cat lick it? (yes/no) \n")
                if cat=="yes":
                    health=input("Is your cat healthy? (yes/no) \n")
                    if health=="yes":
                        print(Ei)
                    elif health=="no":
                        print(Yc)
                elif cat=="no":
                    print(Ei)
        elif st=="no":
            Ema=input("Is it an Emausaurus? (yes/no) \n")
            if Ema=="yes":
                meg=input("Are you a Megalosaurus? (yes/no) \n")
                if meg=="yes":
                    print(Ei)
                elif meg=="no":
                    print(Dne)
            elif Ema=="no":
                cat2=input("Did the cat lick it? (yes/no) \n")
                if cat2=="yes":
                    health2=input("Is your cat healthy? (yes/no) \n")
                    if health2=="yes":
                        print(Ei)
                    elif health2=="no":
                        print(Yc)                
                elif cat2=="no":
                            print(Ei)                 

displayName()   
main()
        