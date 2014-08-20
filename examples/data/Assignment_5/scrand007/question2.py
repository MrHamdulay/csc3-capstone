cost = eval(input("Enter the cost (in cents):\n"))
if cost != 0:
    entered = eval(input("Deposit a coin or note (in cents):\n"))
    new = [entered]
    if entered < cost:
        while sum(new) < cost:
            new.append(eval(input("Deposit a coin or note (in cents):\n")))

    a = sum(new) - cost
    b = a // 100
    c = a - b*100
    d = c // 25
    e = c - d*25
    f = e // 10
    g = e - f*10
    h = g // 5
    i = g - h*5
    j = i // 1
    k = i - j*1
    if a != 0:
        print("Your change is:")
    if b != 0:
        print(b,"x $1")
    if d != 0:
        print(d,"x 25c")
    if f != 0:
        print(f,"x 10c")
    if h != 0:
        print(h,"x 5c")
    if j != 0:
        print(j,"x 1c")