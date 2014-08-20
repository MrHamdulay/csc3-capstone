#program to draw isocles triangle
#Anthony Jacob
#21-March-2014

def main():
    Height=eval(input("Enter the height of the triangle:\n"))
    last=(Height*2)-1      #last line of triangle
    for odd_number in range(1,last+1,2):
        triangle='*'*odd_number
        triangle=triangle.center(last,' ')
        print(triangle)
        

main()