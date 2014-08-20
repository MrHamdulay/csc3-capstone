#Mbongeni Mazibuko
#MZBMBO002
#Assignment 1

hours = int(eval(input('Enter the hours:\n')))
mins = int(eval(input('Enter the minutes:\n')))
seconds = int(eval(input('Enter the seconds:\n'))) 

if (0<=hours<=23) and (0<=mins<=59) and (0<=seconds<=59):
    print('Your time is valid.')
else : print("Your time is invalid.")