def pair(x,y):
    if len(x)>1:
        a = x[0]
        b = x[1]
        if a==b:
            y+=1
            x = x[2:len(x)]
            
            pair(x,y)
        else: 
            x = x[1:len(x)]
            pair(x,y)
    else:
        print('Number of pairs: '+str(y))
              
enter = input('Enter a message:\n')
pair(enter,0)
