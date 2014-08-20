# Assignment 3 Question 3
#Name: Shaheen Karodia
#Student Number: KRDSHA003
#Date 2014-03-20

# program to draw a frame (made of the characters +-|) around a message that has been repeated on consecutive lines.


mess=input("Enter the message:\n")
mess_h=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))

len_mess=len(mess)
a=("|")
b=("+")
c=("-")

x=0


for i in range(thick, 0, -1):
    y=len_mess+2*(i)
    print(x*a, b, y*c, b , x*a, sep="")
    x=x+1
    



for i in range(mess_h):
    print (a*thick ,mess, a*thick)
x=x-1
    
for i in range(1, thick+1):
    y=len_mess+2*(i)
    print(x*a, b, y*c, b , x*a, sep="")
    x=x-1



