#Prac 3 q3
#B.Player
#20/03/2014



def top(t,mes):
    c=0
    for i in range(t):
        print('|'*c,'+','-'*(len(mes)+(t-1)*2-(2*c)),'+','|'*c,sep='')
        c+=1
        
def mess(mes,re,t):
    for i in range(re):
        print('|'*t,mes,'|'*t,sep='')
        
def bot(t,mes):
    c=t-1
    
    for i in range(t,0,-1):
        print('|'*c,'+','-'*(len(mes)+(t-1)*2-(2*c)),'+','|'*c,sep='')
        c-=1
        
        

def main():
    m = " "+input("Enter the message:\n")+" "
    r = eval(input("Enter the message repeat count:\n"))
    th = eval(input("Enter the frame thickness:\n"))    
    top(th,m)
    mess(m,r,th)
    bot(th,m)

main()