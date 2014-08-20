x=int(input("Enter the height of the triangle:\n"))
last = (x * 2) 
for odd_num in range(1, last, 2): 
        y = '*' * odd_num 
        y = y.center(last, ' ') 
        print(y) 




