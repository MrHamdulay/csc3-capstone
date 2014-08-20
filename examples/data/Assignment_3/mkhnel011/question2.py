# Question 2
x=eval(input("Enter the height of the triangle:\n"))
gap=x-1
for i in range(1,x+1,1):
        print(' '*gap,end ='')
        print("*"*(2*i-1))
        gap=gap-1
