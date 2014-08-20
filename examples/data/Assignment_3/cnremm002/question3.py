a=input("Enter the message:\n")
b=eval(input("Enter the message repeat count:\n"))
n=eval(input("Enter the frame thickness:\n"))
string = a
k = 0
for letter in string:
       k = k + 1
def pyramid1(rows=4):
       for i in range(rows):
              print ('|'*(rows+i-n) + '+' + '-'*(2*n-1-2*i+k+1) + '+' + '|'*(rows+i-n)) 
        
pyramid1(n)


for i in range(b):
       print ('|'*(n) + ' ' + (a) + ' ' + '|'*(n))

def pyramid2(rows=5):
       for i in range(rows):
              print ('|'*(rows-i-1) + '+' + '-'*(2*i+1+k+1) + '+' + '|'*(rows-i-1))


pyramid2(n)