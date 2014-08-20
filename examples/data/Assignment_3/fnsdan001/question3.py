text = input("Enter the message:\n")

x = eval(input("Enter the message repeat count:\n"))

y = eval(input("Enter the frame thickness:\n"))


n =  len(text) +2 + 2*y
p = len(text)  + 2

for i in range (y):
    print("|"*i, "+", "-"*(n-2),"+", "|"*i, sep = '')
    n = n-2
for i in range(x):
    print("|"*y, text, "|"*y)

for i in range (y-1,-1,-1):
    print("|"*i, "+", "-"*(p),"+", "|"*i, sep = '')
    p+=2
    
    
    
   
