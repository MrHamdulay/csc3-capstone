height = eval(input("Enter the height of the triangle:\n"))
total = height

for i in range(1,height+height+1,2):
    total -= 1
    if total == 0:
        print("*"*i)
    else:
        print(" "*(total-1),"*"*i)
    