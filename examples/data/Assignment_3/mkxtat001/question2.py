#Tato Moaki MKXTAT001
#Program to draw an isosceles triangle with asterics
#question2 Assignment3

def main():
    height = eval(input("Enter the height of the triangle:\n"))
    
    spacing = height - 1
    for i in range(1, (height * 2), 2):
        print(' '*spacing, end='')
        print('*'*i)
        spacing -= 1
main()