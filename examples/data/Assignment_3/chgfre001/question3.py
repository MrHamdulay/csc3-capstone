def frame(): 

    message=input('Enter the message:\n')
    count=eval(input('Enter the message repeat count:\n'))
    thickness=eval(input('Enter the frame thickness:\n'))

    x=len(message)+thickness*2
    for i in range(0,thickness):
        print('|'*i+'+'+'-'*x+'+'+'|'*i)
        x-=2
        
    for i in range(0,count):
        print(('|'*thickness)+' '+message+' '+('|'*thickness))
    num=thickness-1 
    numChar=len(message)+2
    for i in range(thickness,0,-1):
        print('|'*num+'+'+'-'*numChar+'+'+'|'*num)
        numChar+=2
        num-=1
        
frame()        
    
        
        
        
        
   
