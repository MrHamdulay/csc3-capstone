def main():
    m=input('Enter the message:\n')
    rcount=eval(input('Enter the message repeat count:\n'))
    t=eval(input('Enter the frame thickness:\n'))
    dash=len(m)+(2*t)
    for i in range(t):
        print('|'*i,'+','-'*dash,'+','|'*i,sep='',end='\n')
        dash-=2
        
    for i in range(rcount):
        print('|'*t, m, '|'*t)
        
    for i in range(t-1,-1,-1):
        print('|'*i,'+','-'*(dash+2),'+','|'*i,sep='',end='\n')
        dash+=2
    
main()              