def main():
    n=eval(input("Enter the height of the triangle: \n"))
    gap=n-1
    for i in range(1,n*2,2):
        print(" "*gap,"*"*i,sep='')
        gap=gap-1
main()