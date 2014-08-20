def main():
    x=eval(input("Enter the height of the triangle:\n"))
    y=x
    for i in range(0,x):
        y=y-1
        print(" "*y+(1+2*i)*"*")

main()