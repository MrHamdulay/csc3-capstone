def main():
    a = input("Enter the height of the triangle:\n")
    b = "*"
    x = eval(a)
    y=x-1
    t = (x+y)//2
    for i in range(0,x+y,2):
        print(' '*t,end='')
        print(b*(i+1))
        t-=1
    
main()        
    
    

