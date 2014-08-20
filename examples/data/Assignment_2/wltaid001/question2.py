#Aiden Walton
#WLTAID001
#Cup cake icing flowchart

def main():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    ans1=input("Did anyone see you? (yes/no)\n")
    if ans1=="yes":
        ans1_2=input("Was it a boss/lover/parent? (yes/no)\n")
        if ans1_2=="yes":
            ans2=input("Was it expensive? (yes/no)\n")
            if ans2=="yes":
                ans2_1=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if ans2_1=="yes":
                    print("Decision: Eat it.")
                else: 
                    print("Decision: Your call.")
            else: 
                ans2_2=input("Is it chocolate? (yes/no)\n")
                if ans2_2=="yes":
                    print("Decision: Eat it.")
                else: 
                    print ("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.")                    
    else: 
        ans3=input("Was it sticky? (yes/no)\n")
        if ans3=="yes":
                ans3_1=input("Is it a raw steak? (yes/no)\n")
                if ans3_1=="yes":
                    ans3_2=input("Are you a puma? (yes/no)\n")
                    if ans3_2=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Don't eat it.")
                else:
                    ans4=input("Did the cat lick it? (yes/no)\n")
                    if ans4=="yes":
                        ans4_1=input("Is your cat healthy? (yes/no)\n")
                        if ans4_1=="yes":
                            print("Decision: Eat it.")
                        else:
                            print("Decision: Your call.")
                    else:
                        print("Decision: Eat it.")
        else:
                ans5=input("Is it an Emausaurus? (yes/no)\n")
                if ans5=="yes":
                    ans5_1=input("Are you a Megalosaurus? (yes/no)\n")
                    if ans5_1=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Don't eat it.")
                else:
                    ans4=input("Did the cat lick it? (yes/no)\n")
                    if ans4=="yes":
                        ans4_1=input("Is your cat healthy? (yes/no)\n")
                        if ans4_1=="yes":
                            print("Decision: Eat it.")
                        else:
                            print("Decision: Your call.")
                    else:
                        print("Decision: Eat it.")

main()
    