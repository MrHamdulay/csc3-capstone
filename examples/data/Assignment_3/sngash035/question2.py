x = eval(input("Enter the height of the triangle:\n")) 
last = (x * 2)  
for i in range(1, last,2): 
        line = '*' * i 
        line = line.center(last, ' ') 
        print(line) 