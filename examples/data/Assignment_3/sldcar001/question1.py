def main():
    h=eval(input("Enter the height of the rectangle:\n"))
    w=eval(input("Enter the width of the rectangle:\n"))
    while h>0:
        print("*"*w,sep='')
        h-=1
    
main()