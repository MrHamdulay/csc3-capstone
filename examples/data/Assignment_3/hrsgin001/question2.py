#Enter the height of the triangle:
#5
#    *
#   ***
#  *****
# *******
#*********

h = eval(input("Enter the height of the triangle:\n"))

a=1
for i in range(1, h*2, 2):
    print((h-a)*" ",i*"*", sep ="")
    a+=1
    