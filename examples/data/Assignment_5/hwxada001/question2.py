def main():
    c = eval(input("Enter the cost (in cents):" '\n'))
    d = 0
    while d<c:
        a = eval(input("Deposit a coin or note (in cents):" '\n'))
        d+=a
    ch=d-c
    nc=ch

  
    if ch != 0:
        print("Your change is:")
    if ch >= 100:
        print(ch//100, "x $1")
        nc = ch%100
    if nc >= 25:
        print(nc//25, "x 25c")
        nc = nc%25

    if nc >= 10:
        print(nc//10,"x 10c")
        nc = nc%10            
        
    if nc >= 5:
        print(nc//5, "x 5c")
        nc = nc%5
     
    if nc != 0:
        print(nc//1, "x 1c")
            
main()