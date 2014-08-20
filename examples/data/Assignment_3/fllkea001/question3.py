#Assignment 3
#Question 3
#Keanon Fell
#March 2014
p="+"
d="-"
s="|"
words = input("Enter the message:\n")
r = eval(input("Enter the message repeat count:\n"))
t = eval(input("Enter the frame thickness:\n"))

phrase = " "+ words +" "
length = len(phrase)
length2 = len(words)

y=0
ref1 = length + (t*2)
z=t-1
ref2 = length

if t==1:
    print(p+""+length*d+""+p)
    for i in range(0,r):
        print(s+""+phrase+""+s)
    print(p+""+length*d+""+p) 
elif t>1:
    x = ((t*2) + r)
    
    for i in range(x):
        if(i>=1 and i<=t):
            while y<t:
                print(s*y + "" + p + "" + d*(ref1-2) + "" + p + "" + s*y)
                y+=1
                ref1 -=2
        elif(i>=(t+1) and i <= (x -t)):
            print(s*t + " " + words + " " + s*t)
        elif(i>=(x-(t+1)) and i <+ x):
            while z>=0:
                print(s*z + "" + p + "" + d*(ref2) + "" + p + "" + s*z)
                z-=1
                ref2+=2                