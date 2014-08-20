#Tendani Netshitenzhe
# question 2

height = 2*(eval(input("Enter the height of the triangle:\n")))
gap=height//2
for i in range(0, height, 2):
    print((gap-1)*" ", end="")
    print("*"*(i+1))
    gap-=1
    