msg=input("Enter the message:\n")
r=eval(input("Enter the message repeat count:\n"))
f=eval(input("Enter the frame thickness:\n"))
d=0
h=(len(msg)+2*f)
e=0
t=0
while(d<=2*f):
    
    if(d<f):
        print(d*"|","+",h*"-","+",d*"|",sep="")
        d+=1
        h-=2
        
    elif(d>f):
        
        e-=1
        t+=2         
        print(e*"|","+",t*"-","+",e*"|",sep="")
        d+=1
               
        
    if(d==f):
        for x in range(0,r):
            print(f*"|",msg,f*"|")   
        e=d
        t=h
        d+=1
    