

message = input("Enter the message: \n")
repeat = eval(input("Enter the message repeat count: \n"))
thickness = eval(input("Enter the frame thickness: \n"))

num_dash = len(message) + (2* thickness)

for i in range(thickness):
    print('|' * i , end="")
    print('+', end='')
    print('-' * num_dash , end='')
    print('+' , end="")
    print('|' * i)    
    num_dash -=2
    
gap =" "
    
for i in range(repeat):
    print('|' * thickness, end="")
    print(gap, message, gap, sep="", end="")
    print('|' * thickness)
    
    
num_dash2 = len(message)+2
upright = thickness -1

for i in range(thickness):
    print('|' * (upright), end="")    
    print('+', end='')
    print('-' * num_dash2 ,end="")
    print('+', end="")
    print('|' * upright)
    
    upright-=1
    num_dash2 +=2
    

    
    

    



