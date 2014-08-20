#assignment 3.1

s = "*"
h = eval(input("Enter the height of the rectangle:\n"))
w = eval(input("Enter the width of the rectangle:\n"))

for i in range(1, h+1):
    ans = ""
    for j in range(1,w+1):
        ans = ans+s
    print(ans)

