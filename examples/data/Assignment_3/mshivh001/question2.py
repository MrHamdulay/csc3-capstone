def main():
    h=eval(input("Enter the height of the triangle:\n"))
    w=h
    for i in range(0,h):
        w=w-1
        print(" "*w+(1+2*i)*"*")

main()