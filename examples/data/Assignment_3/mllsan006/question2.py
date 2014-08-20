H = eval(input("Enter the height of the triangle:\n"))
gap = H - 1
n = 1
for i in range (H):
    print(gap*" ", n*"*",sep='')
    n += 2
    gap -= 1