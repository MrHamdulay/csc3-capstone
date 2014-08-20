# Program for printing an isosceles triangle with the "*" symbols
# SHZLWA001 CSC1015F


hgt=eval(input('Enter the height of the triangle:\n'))
space=" "
for i in range(1,hgt+1):
    print(space*(hgt-i)+'*'*(2*i-1))
