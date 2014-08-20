def frame(thick,word):
    x=len(word)+(2*thick)
    for i in range(thick):
        print("|"*i,"+","-"*(x),"+","|"*i,sep='')
        x= x-2
    
        
        

def message(word,repeat,thick):
    for j in range(repeat):
        print("|"*thick,word,"|"*thick)
        
def frame2(thick,word):
    z=len(word)+2
    for i in range(thick,0,-1):
        print("|"*(i-1),"+","-"*z,"+","|"*(i-1),sep="")
        z= z+2
       
        
        
                
if __name__=='__main__':
    word=input("Enter the message:\n")
    repeat=eval(input("Enter the message repeat count:\n"))
    thick=eval(input("Enter the frame thickness:\n"))
    
   
    frame(thick,word)
    message(word,repeat,thick)
    frame2(thick,word)
    