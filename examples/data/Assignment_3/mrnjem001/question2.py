x=eval(input("Enter the height of the triangle:\n"))
base=2*x-1
for i in range(1,2*x,2):
    if i==base:
        print(base*"*")
    else:
        print(((base-i)//2-1)*" ",i*"*")
