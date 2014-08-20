#You dropped your food on the floor, do you eat it?

def main():
    print('Welcome to the 30 Second Rule Expert')
    print('------------------------------------')
    print('Answer the following questions by selecting from among the options.')
    
    yes='yes'
    no='no'
    see=input('Did anyone see you? (yes/no)\n')
    if see==yes:
        blp=input('Was it a boss/lover/parent? (yes/no)\n')
        if blp==no:
            print('Decision: Eat it.')
        if blp==yes:
            expensive=input('Was it expensive? (yes/no)\n')
            if expensive==yes:
                cutoff=input('Can you cut off the part that touched the floor? (yes/no)\n')
                if cutoff==no:
                    print('Decision: Your call.')
                if cutoff==yes:
                    print('Decision: Eat it.')
            if expensive==no:
                chocolate=input('Is it chocolate? (yes/no)\n')
                if chocolate==yes:
                    print('Decision: Eat it.')
                if chocolate==no:
                    print("Decision: Don't eat it.")
    if see==no:
        sticky=input('Was it sticky? (yes/no)\n')
        if sticky==yes:
            steak=input('Is it a raw steak? (yes/no)\n')
            if steak==yes:
                puma=input('Are you a puma? (yes/no)\n')
                if puma==no:
                    print("Decision: Don't eat it.")
                if puma==yes:
                    print('Decision: Eat it.')
            if steak==no:
                cat=input('Did the cat lick it? (yes/no)\n')
                if cat==no:
                    print('Decion: Eat it.')
                if cat==yes:
                    healthy=input('Is your cat healthy? (yes/no)\n')
                    if healthy==no:
                        print('Decision: Your call.')
                    if healthy==yes:
                        print('Decision: Eat it.')
        if sticky==no:
            emausaurus=input('Is it an Emausaurus? (yes/no)\n')
            if emausaurus==no:
                lick=input('Did the cat lick it? (yes/no)\n')
                if lick==no:
                    print('Decision: Eat it.')
                if lick==yes:
                    condition=input('Is your cat healthy? (yes/no)\n')
                    if condition==no:
                        print('Decision: Your call.')
                    if condition==yes:
                        print('Decision: Eat it.')
            if emausaurus==yes:
                megalosaurus=input('Are you a Megalosaurus? (yes/no)\n')
                if megalosaurus==no:
                    print("Decision: Don't eat it.")
                if megalosaurus==yes:
                    print('Decision: Eat it.')
main()

                        
        

                