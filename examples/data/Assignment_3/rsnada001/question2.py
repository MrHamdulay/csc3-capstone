#Adam Rosendorff
#RSNADA001
#CSC1015F - Assignment 3 - Question 2
h = eval(input('Enter the height of the triangle:\n'))
for i in range(h):
    #print(i)
    print('{:^{}}'.format('*'*(2*i+1),2*h))

