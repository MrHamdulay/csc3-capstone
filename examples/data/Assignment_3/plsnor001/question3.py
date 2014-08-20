plus='+'
line='|'
minus='-'
text=input('Enter the message:\n')
count=eval(input('Enter the message repeat count:\n'))
n=eval(input('Enter the frame thickness:\n'))


def top():
    t=len(text)+2*n
    for i in range(n):
        print(line*i+plus+minus*t+plus+line*i)
        t-=2
    for i in range(count):
        print(line*n,text,line*n)
top()

def bottom():
    t=1
    c=n-1

    for i in range(c,-1,-1):
        m=len(text)+2*t
        k=len(text)-2*c

        print(line*i+plus+minus*m+plus+line*i)
        k+=2
        t+=1
bottom()