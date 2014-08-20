# asterix triangle

h = eval(input('Enter the height of the triangle: ''\n'))

def height():
        for i in range(1,h+1):
                gap=(h-i)
                print(gap*' ',end='')
                print((2*i-1)*'*')
        
height()
        

    
    