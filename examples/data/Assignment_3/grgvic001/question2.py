def main():
    rheight = eval(input("Enter the height of the triangle:\n"))
    for i in range(1,rheight+1,1):
        print(" "*(rheight-i),"*"*(2*i-1),sep='')
        
main()       