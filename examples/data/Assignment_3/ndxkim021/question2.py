triheight = eval(input("Enter the height of the triangle:\n")) 
lastline = (triheight * 2)  
for i in range(1, lastline,2): 
        line = '*' * i 
        line = line.center(lastline, ' ') 
        print(line) 