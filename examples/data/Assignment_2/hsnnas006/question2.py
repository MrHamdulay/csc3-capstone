# 30 second rule expert
# 30 second rule expert
# By Nasreen Hoosain
# 10/03/14

eat = "Decision: Eat it."
dont = "Decision: Don't eat it."
call = "Decision: Your call."

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.") #Instructions to user
def cat_lick(): # defines 'did the cat lick it' sequence
    z = input("Did the cat lick it? (yes/no)\n")
    if z == 'no':
        print(eat)
    elif z == 'yes':
        z = input("Is your cat healthy? (yes/no)\n")
        if z == 'no':
            print(call)
        elif z == 'yes':
            print(eat) 
            
def main(): # Main function
    x = input("Did anyone see you? (yes/no)\n")
    if x == "yes": # First branch
        x = input("Was it a boss/lover/parent? (yes/no)\n")
        if x == 'no':
            print(eat)
        elif x == 'yes':
            x = input("Was it expensive? (yes/no)\n")
            if x == 'yes':
                x = input("Can you cut off the part that touched the floor? (yes/no)\n")
                if x == 'yes':
                    print(eat)
                elif x == 'no':
                    print(call)
            elif x == 'no':
                x = input("Is it chocolate? (yes/no)\n")
                if x == 'yes':
                    print(eat)
                elif x == 'no':
                    print(dont)
    elif x == 'no': # 2nd branch
        z = input("Was it sticky? (yes/no)\n")
        if z == 'yes':
            z = input("Is it a raw steak? (yes/no)\n")
            if z == 'yes':
                z = input("Are you a puma? (yes/no)\n")
                if z == 'no':
                    print(dont)
                elif z == 'yes':
                    print(eat)
            elif z == 'no':
                cat_lick() # Runs cat_lick sequence
        elif z == 'no':
            z = input("Is it an Emausaurus? (yes/no)\n")
            if z == 'no':
                cat_lick() # Runs cat_lick sequence
            elif z == 'yes':
                z = input("Are you a Megalosaurus? (yes/no)\n")
                if z == 'yes':
                    print(eat)
                elif z == 'no':
                    print(dont)
        
        
main() # Runs main function