
print("Welcome to the 30 Second Rule Expert\n------------------------------------\nAnswer the following questions by selecting from among the options.")
y="yes"
n="no"
ans=input("Did anyone see you? (yes/no)\n")
if(ans==y):
    ans=input("Was it a boss/lover/parent? (yes/no)\n")
    if(ans==y):
            ans=input("Was it expensive? (yes/no)\n")
            if(ans==y):
                    ans=input("Can you cut off the part that touched the floor? (yes/no)\n")
                    if(ans==y):
                        print("Decision: Eat it.")
                    else:
                        print("Decision: Your call.")
            else:
                ans=input("Is it chocolate? (yes/no)\n")
                if(ans==y):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    ans=input("Was it sticky? (yes/no)\n")
    if(ans==y):
        ans=input("Is it a raw steak? (yes/no)\n")
        if(ans==y):
            ans=input("Are you a puma? (yes/no)\n")
            if(ans==y):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            ans=input("Did the cat lick it? (yes/no)\n")
            if(ans==y):
                ans=input("Is your cat healthy? (yes/no)\n")
                if(ans==y):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        ans=input("Is it an Emausaurus? (yes/no)\n")
        if(ans==y):
            ans=input("Are you a Megalosaurus? (yes/no)\n")
            if(ans==y):
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            ans=input("Did the cat lick it? (yes/no)\n")
            if(ans==y):
                ans=input("Is your cat healthy? (yes/no)\n")
                if(ans==y):
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
        
                    