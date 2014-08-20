# Question 2 Assignment 2
# Author: Julius Stopforth STPJUL004
# Date: 10/03/2014

print('Welcome to the 30 Second Rule Expert')
print('------------------------------------')
print('Answer the following questions by selecting from among the options.')

response = input("Did anyone see you? (yes/no)\n")
decision = 'There was an error with a response'

if response == 'yes':
    response = input("Was it a boss/lover/parent? (yes/no)\n")
    if response == 'yes':
        response = input("Was it expensive? (yes/no)\n")
        if response == 'yes':
            response = input("Can you cut off the part that touched the floor? (yes/no)\n")
            if response == 'yes':
                    decision = 'Eat it.'
            elif response == 'no':
                    decision = 'Your call.'            
        elif response == 'no':
            response = input("Is it chocolate? (yes/no)\n")
            if response == 'yes':
                decision = 'Eat it.'
            elif response == 'no':
                decision = 'Don\'t eat it.'               
    elif response == 'no':
        decision = 'Eat it.'
elif response == 'no':
    response = input("Was it sticky? (yes/no)\n")
    if response == 'yes':
        response = input("Is it a raw steak? (yes/no)\n")
        if response == 'yes':
            response = input("Are you a puma? (yes/no)\n")
            if response == 'yes':
                decision = 'Eat it.'
            elif response == 'no':
                decision = 'Don\'t eat it.'            
        elif response == 'no':
            response = input("Did the cat lick it? (yes/no)\n") 
            if response == 'yes':
                response = input("Is your cat healthy? (yes/no)\n")
                if response == 'yes':
                    decision = 'Eat it.'
                elif response == 'no':
                    decision = 'Your call.'               
            elif response == 'no':
                decision = 'Eat it.'           
    elif response == 'no':
        response = input("Is it an Emausaurus? (yes/no)\n")
        if response == 'yes':
            response = input("Are you a Megalosaurus? (yes/no)\n")
            if response == 'yes':
                decision = 'Eat it.'
            elif response == 'no':
                decision = 'Don\'t eat it.'            
        elif response == 'no':
            response = input("Did the cat lick it? (yes/no)\n") 
            if response == 'yes':
                response = input("Is your cat healthy? (yes/no)\n")
                if response == 'yes':
                    decision = 'Eat it.'
                elif response == 'no':
                    decision = 'Your call.'               
            elif response == 'no':
                decision = 'Eat it.'        
        
print('Decision:', decision)