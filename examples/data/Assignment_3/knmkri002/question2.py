# Isoceles triangle creator
# Kristin Kinmont
# 21 March 2014

x = eval(input("Enter the height of the triangle:\n"))
for i in range(x):
    space=x-1
    i=2*i+1
    print(' '*space+'*'*i)
    x-=1
