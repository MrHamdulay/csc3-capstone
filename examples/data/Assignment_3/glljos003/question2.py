x = int(input("Enter the height of the triangle: ")) 
last = (x * 2) - 1 
for odd_num in range(-1, last+1, 2): 
        line = '*' * odd_num 
        line = line.center(last, ' ') 
        print(line) 