def main():  
    rheight = eval(input("Enter the height of the rectangle:\n"))
    rwidth = eval(input("Enter the width of the rectangle:\n"))
    for i in range(rheight):
        print("*"*rwidth,end="\n",sep='')
main()