mes = input('Enter the message: \n')
rep = eval(input('Enter the message repeat count: \n'))
thick = eval(input("Enter the frame thickness: \n"))

dash= '-'
y = len(mes) + 2*thick

for i in range(0, thick):
    print('|' * i, end="")
    print('+', end="")
    print(dash * y, end="")
    print('+', end="")
    print('|' * i)
    y -=2
    
gap=" "
    
for i in range(rep):
    print('|' * thick, end="")
    print(gap, end="")
    print(mes, end="")
    print(gap, end="")
    print('|' * thick)
    
    
y2 =  len(mes) + 2
upline=  thick -1

for i in range(thick):
    print('|' * upline, end="")
    print('+' , end="")
    print(dash * y2, end="")
    print('+', end="")
    print('|' * upline)
    
    y2 +=2
    upline -=1
    
    
    