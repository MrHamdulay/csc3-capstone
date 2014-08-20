#Assignment 3 - Question 3
#Jayan Smart
#20 March 2014
x=input("Enter the message:\n") #the message to be printed
n=len(x) #number of charaters to be printed
c = eval(input("Enter the message repeat count:\n")) #the number of times that the message will be repeated
w = eval(input("Enter the frame thickness:\n")) #the tickness of the frame
i=1

for i in range(1,w+1):
    print(('|'*(i-1))+('+')+('-'*(n+2*((w-i)+1))+('+')+('|'*(i-1))))
    i+=1
while i>w and i<=(c+w):
    print(('|'*w)+" "+x+" "+'|'*w)
    i+=1
for i in range(w+1,1,-1):
    print(('|'*(i-2))+('+')+('-'*(n+2*((w-i)+2))+('+')+('|'*(i-2))))
    i+=1
