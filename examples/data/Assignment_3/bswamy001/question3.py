a=input("Enter the message:\n")
b=eval(input("Enter the message repeat count:\n"))
c=eval(input("Enter the frame thickness:\n"))

print('+', '-'*(len(a)+(c*2)), '+', sep='')
x=len(a)+(c*2)
for i in range(1,c): 
    x-=2
    print(i*'|', '+', '-'*x, '+', i*'|', sep='')

for j in range(1,b+1):
    print('|'*c, a, '|'*c)
    
x=len(a)
for i in range(c-1,0,-1): 
    x+=2
    print(i*'|', '+', '-'*x, '+', i*'|', sep='')
    
print('+', '-'*(len(a)+(c*2)), '+', sep='')






    
    



        

