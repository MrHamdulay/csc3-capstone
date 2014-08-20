# A program which asks a series of questions to determine if you should eat food that has fallen onto the ground
#Author: Emiel Zyde
#Date: 6 March 2014

def intro():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")    
    
def main():
    intro()
    ans_1=input("Did anyone see you? (yes/no)\n")
    if ans_1=="yes":
        ans_2=input("Was it a boss/lover/parent? (yes/no)\n")
        if ans_2=="yes":
            ans_3=input("Was it expensive? (yes/no)\n")
            if ans_3=="yes":
                ans_4=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if ans_4=="yes":
                    print("Decision: Eat it.")
                elif ans_4=="no":
                    print("Decision: Your call.")
            elif ans_3=="no":
                ans_5=input("Is it chocolate? (yes/no)\n")
                if ans_5=="yes":
                    print("Decision: Eat it.")
                elif ans_5=="no":
                    print("Decision: Don't eat it.")
        elif ans_2=="no":
            print("Decision: Eat it.")  
    elif ans_1=="no":
        ans_6=input("Was it sticky? (yes/no)\n")
        if ans_6=="yes":
            ans_7=input("Is it a raw steak? (yes/no)\n")
            if ans_7=="yes":
                ans_8=input("Are you a puma? (yes/no)\n")
                if ans_8=="yes":
                    print("Decision: Eat it.")
                elif ans_8=="no":
                    print("Decision: Don't eat it.")
            elif ans_7=="no":
                ans_9=input("Did the cat lick it? (yes/no)\n")
                if ans_9=="yes":
                    ans_10=input("Is your cat healthy? (yes/no)\n")
                    if ans_10=="yes":
                        print("Decision: Eat it.")
                    elif ans_10=="no":
                        print("Decision: Your call.")
                elif ans_9=="no":
                    print("Decision: Eat it.")
        elif ans_6=="no":
            ans_11=input("Is it an Emausaurus? (yes/no)\n")
            if ans_11=="yes":
                ans_12=input("Are you a Megalosaurus? (yes/no)\n")
                if ans_12=="yes":
                    print("Decision: Eat it.")
                elif ans_12=="no":
                    print("Decision: Don't eat it.")
            elif ans_11=="no":
                ans_9=input("Did the cat lick it? (yes/no)\n")
                if ans_9=="yes":
                    ans_10=input("Is your cat healthy? (yes/no)\n")
                    if ans_10=="yes":
                        print("Decision: Eat it.")
                    elif ans_10=="no":
                        print("Decision: Your call.")
                elif ans_9=="no":
                    print("Decision: Eat it.")                

main()


            