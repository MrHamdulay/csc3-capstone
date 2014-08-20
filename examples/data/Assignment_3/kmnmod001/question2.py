def main():
    height = eval(input("Enter the height of the triangle:\n"))
    width = height-1
    b = height + 1
    a = 1
    for i in range (1,b):
        print(" "*width+"*"*a)
        width = width -1
        a += 2
main()