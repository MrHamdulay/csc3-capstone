#character triangle

x=eval(input("Enter the height of the triangle:\n"))
y=2*x-1
gap=y//2

for i in range(0,y,2):
    print(' '*gap,end='')  
    print("*"*(i+1))
    gap=gap-1