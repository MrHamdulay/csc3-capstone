validity = 'invalid.'
hours = eval(input('Enter the hours:\n'))
minutes = eval(input('Enter the minutes:\n'))
seconds = eval(input('Enter the seconds:\n'))

if 0 <= hours <= 23:
    if 0 <= minutes <= 60:
        if 0 <= seconds <= 60:
            validity = 'valid.'

print('Your time is',validity)
           
    

    