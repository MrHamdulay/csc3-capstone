def main():
    h = eval(input("Enter the height of the triangle:\n"))
    for i in range(1,h+1):
        l = " "*((1+2*((h+1)-1))//2-i)
        l += "*"*(1+2*(i-1))
        print(l)
main()                     