#Prac 3 q2
#B.Player
#16/03/2014

h=eval(input("Enter the height of the triangle:\n"))
gap=h-1

for i in range(1,h+1):
    print(gap*" ",end='')
    print('*'*((i*2)-1))
    gap-=1