# Program to draw frame around a message
# Khwezi Majola
# MJLKHW001
# 20 March 2014
def frame():
    message = input('Enter the message:\n')
    repeat = eval(input('Enter the message repeat count:\n'))
    thick = eval(input('Enter the frame thickness:\n'))
    length = len(message) + 2
    for i in range(thick):
        print('|' * i + '+' + '-' * (length+thick*2 - 2*(i+1)) + '+' +'|' * i)
    for i in range(repeat):
        print('|' * thick + ' ' + message + ' ' + '|' * thick) 
    for i in range(thick - 1, -1, -1):
            print('|' * i + '+' + '-' * (length+thick*2 - 2*(i+1)) + '+' +'|' * i)    
frame()