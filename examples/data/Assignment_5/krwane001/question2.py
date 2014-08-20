paid=0
c=eval(input("Enter the cost (in cents):\n"))

while paid < c:
    more=eval(input("Deposit a coin or note (in cents):\n"))
    paid=paid+more
    
change=paid-c
if paid > c:
    print("Your change is:")
    while change > 0:
        if change >= 100:
            z = change//100
            change = change-(z*100)
            print(z, "x $1")
            if change ==0:
                break
        if change >= 25:
            y = change//25
            change=change-(y*25)
            print(y, "x 25c")
            if change ==0:
                break
        if change >= 10:
            x = change//10
            change=change-(x*10)
            print(x, "x 10c")
            if change ==0:
                break
        if change >= 5:
                w = change//5
                change=change-(w*5)
                print(w, "x 5c")
                if change ==0:
                    break
        if change >= 1:
                y = change//1
                change=change-(y*1)
                print(y, "x 1c")
                if change ==0:
                    break
                