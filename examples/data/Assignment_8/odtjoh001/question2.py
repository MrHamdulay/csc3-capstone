def loop(message,n):
    if len(message) <2:
        print(n)
    elif message[0] == message [1]:
        n += 1 
        return loop(message[2:],n)
    else:
        return loop(message[2:],n)
mes = input("Enter a message:\n")
print("Number of pairs: " ,end = "")
loop(mes,0)