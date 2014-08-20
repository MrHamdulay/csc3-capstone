#Program to determine whether or not you should eat the food you dropped.
#Tsanwani Vhonani
#09 March 2014

def The_30_second_rule_expert():
    a="yes"
    b="no"
    print("Welcome to the 30 Second Rule Expert")
    print("-"*36)
    print("Answer the following questions by selecting from among the options.")
    ans=input("Did anyone see you? (yes/no)\n")
    if ans==a:
        ans=input("Was it a boss/lover/parent? (yes/no)\n")
        if ans==a:
            ans=input("Was it expensive? (yes/no)\n") 
            if ans==a:
                ans=input("Can you cut off the part that touched the floor? (yes/no)\n")
                if ans==a:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                ans=input("Is it chocolate? (yes/no)\n")
                if ans==a:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
        else:
            print("Decision: Eat it.\n")
    else:
        ans=input("Was it sticky? (yes/no)\n")
        if ans==a:
            ans=input("Is it a raw steak? (yes/no)\n")
            if ans==a:
                ans=input("Are you a puma? (yes/no)\n")
                if ans==a:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                ans=input("Did the cat lick it? (yes/no)\n")
                if ans==a:
                    ans=input("Is your cat healthy? (yes/no)\n")
                    if ans==a:
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
        else:
            ans=input("Is it an Emausaurus? (yes/no)\n")
            if ans==a:
                ans=input("Are you a Megalosaurus? (yes/no)\n")
                if ans==a:
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
            else:
                ans=input("Did the cat lick it? (yes/no)\n")
                if ans==a:
                    ans=input("Is your cat healthy? (yes/no)\n")
                    if ans==a:
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
                else:
                    print("Decision: Eat it.")
                    
                        
                    
The_30_second_rule_expert()

                    
                    
    
    
    
    