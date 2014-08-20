x=input("Enter the message:\n")
t=eval(input("Enter the message repeat count:\n"))
y=eval(input("Enter the frame thickness:\n"))
mins=len(x)+(2*y)
plus=0
slash=0

for i in range(y):
 print("|"*slash,"+","-"*mins,"+","|"*slash,sep="") 
 mins=mins-2
 slash=slash+1
for i in range(t):
 print("|"*y,x,"|"*y)

for i in range(y):
 mins=mins+2
 slash=slash-1  
 print("|"*slash,"+","-"*mins,"+","|"*slash,sep="") 
 

