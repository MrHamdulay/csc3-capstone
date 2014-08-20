import math
function = input("Enter a function f(x):\n")

y = [0] * 21

for i in range(-10, 11):
    f = function.replace('x', "("+str(i)+")")
    y[i+10] = eval(f)

for coord_y in range(21):
    for coord_x in range(21):
        if round(y[coord_x]-1) == -1*(coord_y-9):
            print('o', end='')
        elif coord_y == 10 and coord_x == 10:
            print('+', end='')
        elif coord_y == 10:
            print('-', end='')
        elif coord_x == 10:
            print('|', end='')
        else:
            print(' ', end = '')
    print('')
                        
                            
