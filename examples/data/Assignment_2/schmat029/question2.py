#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Matthias
#
# Created:     07-03-2014
# Copyright:   (c) Matthias 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

if input("Did anyone see you? (yes/no) \n") == "yes":
    if input("Was it a boss/lover/parent? (yes/no) \n") == "yes":
        if input("Was it expensive? (yes/no) \n") == "yes":
            if input("Can you cut off the part that touched the floor? (yes/no) \n") == "yes":
                print("Decision: Eat it.")
            else: # no for cut off part
                print("Decision: Your call.")
        else: # no for expensive
            if input("Is it chocolate? (yes/no) \n") == "yes":
                print("Decision: Eat it.")
            else: # no for chocolate
                print("Decision: Don't eat it.")
    else: # no for boss/lover/parent
        print("Decision: Eat it.")
else: # no for seeing
    if input("Was it sticky? (yes/no) \n") == "yes":
        if input("Is it a raw steak? (yes/no) \n") == "yes":
            if input("Are you a puma? (yes/no) \n") == "yes":
                print("Decision: Eat it.")
            else: # no for puma
                print("Decision: Don't eat it.")
        else: # no for steak
            if input("Did the cat lick it? (yes/no) \n") == "yes":
                if input("Is your cat healthy? (yes/no) \n") == "yes":
                    print("Decision: Eat it.")
                else: # no for healthy cat
                    print("Decision: Your call.")
            else: # no for cat licking
                print("Decision: Eat it.")
    else: # no for stickyness
        if input("Is it an Emausaurus? (yes/no) \n") == "yes":
            if input("Are you a Megalosaurus? (yes/no) \n") == "yes":
                print("Decision: Eat it.")
            else: # no for megalosaurus
                print("Decision: Don't eat it.")
        else: # no for emausaurus
            if input("Did the cat lick it? (yes/no) \n") == "yes":
                if input("Is your cat healthy? (yes/no) \n") == "yes":
                    print("Decision: Eat it.")
                else: # no for healthy cat
                    print("Decision: Your call.")
            else: # no for cat licking
                print("Decision: Eat it.")

if __name__ == '__main__':
    main()
