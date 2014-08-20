
def makeTri(hight):
    width = (hight*2)-1
    gap = width//2
    count = 0

    for i in range(0,width,2):
        print(" "*gap,end="")
        gap= gap -1
        print("*"*(i+1))
        count = count +2
        
  
hi = eval(input("Enter the height of the triangle:\n"))
makeTri(hi)
        