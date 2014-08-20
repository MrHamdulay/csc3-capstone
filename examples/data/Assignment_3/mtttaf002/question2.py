#creating a triangle with height n
#created by tafara mtutu
#23 march 2013
def isosceles(n):
        s = "*"
        for i in range(1,n+1,1):
                print(" "*(n-i), s, sep = "")
                s+="**"
height = eval(input("Enter the height of the triangle:\n"))
isosceles(height)