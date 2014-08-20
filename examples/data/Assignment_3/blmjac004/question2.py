x=eval(input("Enter the height of the triangle:\n"))
w=1
for i in range(x):
    gap= " "*(x-i-1)
    print(gap,"*"*w, sep='')
    w=w+2
    