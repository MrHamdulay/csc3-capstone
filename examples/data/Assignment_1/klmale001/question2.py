hours=input('Enter the hours:\n')
hours=eval(hours)
minutes=input('Enter the minutes:\n')
minutes=eval(minutes)
seconds=input('Enter the seconds:\n')
seconds=eval(seconds)
if((0<=hours<=24) and (0<=minutes<=60) and (0<=seconds<=60)):
    print('Your time is valid.')
else: 
        print('Your time is invalid.')