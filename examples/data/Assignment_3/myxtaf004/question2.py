h=eval(input("Enter the height of the triangle:\n"))
x=-1
a=-1
char="*"
for i in range(h):
    x=x+2


for i in range(h):
    a=a+2
    print(char.center(x))
    char=char+"*"*2