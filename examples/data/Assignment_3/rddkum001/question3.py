def frame(M,R,T):
    for i in range(T):
            print('|'*i,'+','-'*(len(M)+2*T),'+','|'*i,sep='')
            T=T-1

def message(M,R,T):
    for i in range(R):
        print('|'*T,M,'|'*T)
        
def frame2(M,R,T):
    for i in range(T):
        print('|'*(T-1),'+','-'*(len(M)+2*(i+1)),'+','|'*(T-1),sep='')
        T=T-1
        
if __name__=='__main__':
    M=input("Enter the message:\n")
    R=eval(input("Enter the message repeat count:\n"))
    T=eval(input("Enter the frame thickness:\n"))
    frame(M,R,T)
    message(M,R,T)
    frame2(M,R,T)

 