hight = eval(input("Enter the height of the triangle:\n"))

for i in range (1, hight+1):
    print(" "*(hight-(i)) + "*"*(2*(i)-1), end = "\n")