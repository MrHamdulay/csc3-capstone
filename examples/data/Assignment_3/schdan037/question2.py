def isos(h):
    gap = " "*(h-1)
    for i in range(h):
        print(gap, "*"*(i*2 + 1), sep = "")
        gap = gap[:len(gap) - 1]
        
if __name__ == "__main__":
    n = eval(input("Enter the height of the triangle: \n"))
    isos(n)
