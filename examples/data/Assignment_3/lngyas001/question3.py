x = input('Enter the message:\n')
message = eval(input('Enter the message repeat count:\n'))
thick = eval(input('Enter the frame thickness:\n'))

m = len(x)+thick*2 #amount of - = length of string * 2xthickness
for i in range (thick): #print specified frame thickness
    print('|'*i,'+',m*'-','+','|'*i, sep = '') #to print top frame
    m-=2 #amount of - decreases by 2 with each iteration
    
for j in range (message): #print message out specified number of times
    print('|'*thick, x, '|'*thick) #print message and corrosponding number of bars

m = len(x)+2 #no. of - = length of string + 2
for k in range (thick-1,-1,-1): #reversing the range
    print('|'*k,'+',m*'-','+','|'*k, sep = '') #print bottom frame
    m+=2 #amount of - increases by 2 with each iteration
    
    
    
       
