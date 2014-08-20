def time():    
    x=(eval(input("Enter the hours:")))
    while((x<0)or(x>23)):
        print("Your time is invalid")
        x=(eval(input(" Enter the hours:")))
    y=(eval(input("Enter the minutes:")))
    while((y<0)or(y>59)):
            print("Your time is invalid")
            y=(eval(input("Enter the minutes:")))    
    d=(eval(input("Enter the seconds:")))
    while((d<0)or(d>59)):
            print("Your time is invalid")
            d=(eval(input("Enter the seconds:")))  
    print("the time is",x,y,d,sep=":")

if __name__=='__main__':
    time()