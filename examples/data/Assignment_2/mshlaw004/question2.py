def main():
    q1=input("Did anyone see you? (yes/no)\n")
    if q1=="yes":
        q2=input("Was it a boss/lover/parent? (yes/no)\n")
        if q2=="yes":
            q3=input("Was it expensive? (yes/no)\n")
            if q3=="yes":
                q4=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if q4=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                p1=input("Is it chocolate? (yes/no)\n")
                if p1=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")
    else :
        p2=input("Was it sticky? (yes/no)\n")
        if (p2=="yes"):
            p2=input("Is it a raw steak? (yes/no)\n")
            if p2=="yes":
                p3=input("Are you a puma? (yes/no)\n")
                if p3=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                x1=input("Did the cat lick it? (yes/no)\n")
                if x1=="yes":
                    x2=input("Is your cat healthy? (yes/no)\n")
                    if x2=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                    
                else:
                    print("Decision: Eat it.")
        else:
            k1=input("Is it an Emausaurus? (yes/no)\n")
            if k1=="yes":
                k2=input("Are you a Megalosaurus? (yes/no)\n")
                if k2=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                k3=input("Did the cat lick it? (yes/no)\n")
                if k3=="yes":
                    k4=input("Is your cat healthy? (yes/no)\n")
                    if k4=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")


print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
main()









        
