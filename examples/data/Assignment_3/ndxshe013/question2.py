def main():
    
    height = eval(input("Enter the height of the triangle:\n"))
    for i in range(1,height+1):
        print(" "*(height-i)+"*"*i+"*"*(i-1))
        
main()