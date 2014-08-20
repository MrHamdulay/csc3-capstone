# Shanice Sewnarain
# SWNSHA007
# A program to decide whether or not you should eat the food or not.
# 9 March 2014
# By: Shanice Sewnarain

def main():
    print("Welcome to the 30 Second Rule Expert")
    print("------------------------------------")
    print("Answer the following questions by selecting from among the options.")
    x=input("Did anyone see you? (yes/no)\n")
    if x=="yes":
        y=input("Was it a boss/lover/parent? (yes/no)\n")    
        if y=="yes":
            b=input("Was it expensive? (yes/no)\n")
            if b=="yes":
                c=input("Can you cut off the part that touched the floor? (yes/no)\n")  
                if c=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.") 
            else:
                d=input("Is it chocolate? (yes/no)\n")
                if d=="yes":
                    print("Decision: Eat it.")  
                else:
                    print("Decision: Don't eat it.")  
        else:
            print("Decision: Eat it.")               
    else:
        z=input("Was it sticky? (yes/no)\n")
        if z=="yes":
            e=input("Is it a raw steak? (yes/no)\n")
            if e=="yes":
                f=input("Are you a puma? (yes/no)\n")
                if f=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")                
            else:
                g=input("Did the cat lick it? (yes/no)\n")
                if g=="yes":
                    q=input("Is your cat healthy? (yes/no)\n")
                    if q=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")                
        else:
            n=input("Is it an Emausaurus? (yes/no)\n")
            if n=="yes":
                k=input("Are you a Megalosaurus? (yes/no)\n")
                if k=="yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                g=input("Did the cat lick it? (yes/no)\n") 
                if g=="yes":
                    q=input("Is your cat healthy? (yes/no)\n")
                    if q=="yes":
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
                                                
                                                                                    
main()


