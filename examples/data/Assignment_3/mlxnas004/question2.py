#nasha meoli
#21st march 2014
#program to print isosceles
height = eval(input("Enter the height of the triangle:\n"))


def triangle(height):
    gap2 = height-1
    star = 1
    for i in range(height):
        gap = gap2*" "
        print(gap+star*"*")
        gap2=gap2-1
        star+=2
        
triangle(height)
