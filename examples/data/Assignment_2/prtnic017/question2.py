# Student Number: PRTNIC017
# Date: 3/7/14

# messages
msg_eat = 'Decision: Eat it.'
msg_no_eat = 'Decision: Don\'t eat it.'
msg_maybe = 'Decision: Your call.'

# function
def yes(x) -> bool:
    return x == 'yes'


# welcome
print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

# start questioning
# DID ANYONE SEE YOU?
a = input('Did anyone see you? (yes/no)\n')
if yes(a):
    # WAS IT A BOSS/LOVER/PARENT?
    a = input('Was it a boss/lover/parent? (yes/no)\n')
    if yes(a):
        # WAS IT EXPENSIVE?
        a = input('Was it expensive? (yes/no)\n')
        if yes(a):
            # CAN YOU CUT OFF TOUCH PART?
            a = input('Can you cut off the part that touched the floor? (yes/no)\n')
            if yes(a):
                print(msg_eat)
            else:
                print(msg_maybe)
        else:
            # IS IT CHOCOLATE?
            a = input('Is it chocolate? (yes/no)\n')
            if yes(a):
                print(msg_eat)
            else:
                print(msg_no_eat)
    else:
        print(msg_eat)
else:
    # WAS IT STICKY?
    a = input('Was it sticky? (yes/no)\n')
    if yes(a):
        # IS IT A RAW STEAK?
        a = input('Is it a raw steak? (yes/no)\n')
        if yes(a):
            # ARE YOU A PUMA?
            a = input('Are you a puma? (yes/no)\n')
            if yes(a):
                print(msg_eat)
            else:
                print(msg_no_eat)
        else:
            # DID THE CAT LICK IT?
            a = input('Did the cat lick it? (yes/no)\n')
            if yes(a):
                # IS YOUR CAT HEALTHY?
                a = input('Is your cat healthy? (yes/no)\n')
                if yes(a):
                    print(msg_eat)
                else:
                    print(msg_maybe)
            else:
                print(msg_eat)
    else:
        # IS IT AN EMAUSAURUS?
        a = input('Is it an Emausaurus? (yes/no)\n')
        if yes(a):
            # ARE YOU A MEGALOSAURUS?
            a = input('Are you a Megalosaurus? (yes/no)\n')
            if yes(a):
                print(msg_eat)
            else:
                print(msg_no_eat)
        else:
            # DID THE CAT LICK IT?
            a = input('Did the cat lick it? (yes/no)\n')
            if yes(a):
                # IS YOUR CAT HEALTHY?
                a = input('Is your cat healthy? (yes/no)\n')
                if yes(a):
                    print(msg_eat)
                else:
                    print(msg_maybe)
            else:
                print(msg_eat)