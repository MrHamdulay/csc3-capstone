# a program that draws an isosceles triangle of a given height
# xola gcwabe
# 18/04/2014

# prompting user to enter the height of the triangle
height = input("Enter the height of the triangle:\n")
# converting the user's input to an integer
height = eval(height)
for i in range(1,height+1):
    print((height - i)*' ','*'*i, (i-1)*'*', sep ='')