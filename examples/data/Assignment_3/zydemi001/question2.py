def main():
    Height = eval(input("Enter the height of the triangle:\n"))
    height = 2*Height
    star = "*"
    for i in range (Height):
        print(star.center(height))
        star = star+2*"*"

main()