
eat = 'Decision: Eat it.'
don_eat = 'Decision: Don\'t eat it.'
maybe = 'Decision: Your call.'


def yes(x):
    if x.lower() == 'yes':
        return True
    else:
        return False


print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

ans = input('Did anyone see you? (yes/no)\n')
if yes(ans):
    ans = input('Was it a boss/lover/parent? (yes/no)\n')
    if yes(ans):
        ans = input('Was it expensive? (yes/no)\n')
        if yes(ans):
            ans = input('Can you cut off the part that touched the floor? (yes/no)\n')
            if yes(ans):
                print(eat)
            else:
                print(maybe)
        else:
            ans = input('Is it chocolate? (yes/no)\n')
            if yes(ans):
                print(eat)
            else:
                print(don_eat)
    else:
        print(eat)
else:
    ans = input('Was it sticky? (yes/no)\n')
    if yes(ans):
        ans = input('Is it a raw steak? (yes/no)\n')
        if yes(ans):
            ans = input('Are you a puma? (yes/no)\n')
            if yes(ans):
                print(eat)
            else:
                print(don_eat)
        else:
            ans = input('Did the cat lick it? (yes/no)\n')
            if yes(ans):
                ans = input('Is your cat healthy? (yes/no)\n')
                if yes(ans):
                    print(eat)
                else:
                    print(maybe)
            else:
                print(eat)
    else:
        ans = input('Is it an Emausaurus? (yes/no)\n')
        if yes(ans):
            ans = input('Are you a Megalosaurus? (yes/no)\n')
            if yes(ans):
                print(eat)
            else:
                print(don_eat)
        else:
            ans = input('Did the cat lick it? (yes/no)\n')
            if yes(ans):
                ans = input('Is your cat healthy? (yes/no)\n')
                if yes(ans):
                    print(eat)
                else:
                    print(maybe)
            else:
                print(eat)