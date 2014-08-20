#question2
#Paul Truter
#25 March 2014

n=eval(input("Enter the height of the triangle:\n"))

spaces=n-1
width=n*2+1
a=" "
b='*'
for i in range(1,width,2):
    line=a*spaces+b*i+a*(spaces)
    spaces-=1
    print(line)
    