# Question 2
#BY: Dean de Haast

height = eval(input("Enter the height of the triangle:\n"))
i = 1
spaces = height-1


while i<height+1:
    
    print(spaces*(" "),((i*2)-1)*"*",sep="")
    i += 1
    spaces = spaces - 1  