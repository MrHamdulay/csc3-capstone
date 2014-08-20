height = eval(input("Enter the height of the triangle: \n"))
t=1
s=' '
m=height-1
for i in '*'*(height):
    print(s*m,i*t,sep='')
    t+=2
    m-=1