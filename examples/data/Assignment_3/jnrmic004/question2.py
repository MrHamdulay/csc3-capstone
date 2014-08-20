def main():
    height = int(input("Enter the height of the triangle:\n"))
    tot = height*2 -1
    star = 1
    space = tot//2
    for i in range(height):
        if height!=i:print(" "*space,end="")
        print("*"*star," "*space)
        star += 2
        space -= 1
        
main()