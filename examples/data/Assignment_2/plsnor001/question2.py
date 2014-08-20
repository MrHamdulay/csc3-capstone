def main():
    print("Welcome to the 30 Second Rule Expert")
    print('------------------------------------')
    print('Answer the following questions by selecting from among the options.')

    e='Eat it.'
    d="Don't eat it."
    y='Your call.'

    one=input('Did anyone see you? (yes/no)\n')
    if one=='yes':
        three=input('Was it a boss/lover/parent? (yes/no)\n')

        if three=='yes':
            four=input('Was it expensive? (yes/no)\n')
            if four=='yes':
                five=input('Can you cut off the part that touched the floor? (yes/no)\n')
                if five=='yes':
                    print('Decision:',e)
                else:
                    print('Decision:',y)
            else:
                ten=input('Is it chocolate? (yes/no)\n')
                if ten=='yes':
                    print('Decision:',e)
                else:
                    print('Decision:',d)

        else: print('Decision:',e)



    else:
        two=input('Was it sticky? (yes/no)\n')
        if two=='yes':
            six=input('Is it a raw steak? (yes/no)\n')
            if six=='yes':
                nine=input('Are you a puma? (yes/no)\n')
                if nine=='yes':
                    print('Decision:',e)
                else: print('Decision:',d)
            else:
                eight=input('Did the cat lick it? (yes/no)\n')
                if eight=='yes':
                    eleven=input('Is your cat healthy? (yes/no)\n')
                    if eleven=='yes':
                        print('Decision:',e)
                    else: print('Decision:',y)

                else:
                    print('Decision:',e)



        else:
            twelve=input('Is it an Emausaurus? (yes/no)\n')
            if twelve=='yes':
                seven=input('Are you a Megalosaurus? (yes/no)\n')
                if seven=='yes':
                    print('Decision:',e)
                else: print('Decision:',d)
            else:
                eight=input('Did the cat lick it? (yes/no)\n')
                if eight=='yes':
                    eleven=input('Is your cat healthy? (yes/no)\n')
                    if eleven=='yes':
                        print('Decision:',e)
                    else: print('Decision:',y)
                else:
                    print('Decision:',e)
if __name__ == '__main__':
    main()
