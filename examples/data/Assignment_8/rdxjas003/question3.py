def cript(x,y):
    if y<len(x):
        a = ord(x[y])  
        b = x[0:y]
        c = x[y+1:len(x)]
        if a==122:
            a = 97
        elif a == 32:
            a+=0
        elif 65<a<90:
            a+=0
        elif a == 46:
            a+=0
        else:
            a+=1
        x = b + chr(a) + c
        y+=1
        cript(x,y)  
    else:
        print('Encrypted message:\n'+x)
enter = input('Enter a message:\n')
cript(enter,0)