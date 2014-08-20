def frame():
    x=(input('Enter the message:\n'))
    y=eval(input('Enter the message repeat count:\n'))
    z=eval(input('Enter the frame thickness:\n'))
    a=len(x)+(2*(z))
    c=0
 
   

    for i in range (z):
        print('|'*c,'+','-'*a,'+','|'*c,sep='')
        a-=2
        c+=1
    for f in range(y):
        print('|'*z,' ',x,' ','|'*z,sep='')
        
    c=c-1
    for i in range(z):
        
        
        print('|'*c,'+','-'*(len(x)+2+(2*(i))),'+','|'*c,sep='')
        c-=1
     
        
        
        
       
       
       
      
      
   
        
    
    
frame()        