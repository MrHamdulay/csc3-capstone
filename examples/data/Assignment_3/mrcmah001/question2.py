x = int(input("Enter the height of the triangle:"'\n')) 
last = (x * 2)  
for odd_num in range(1, last, 2): 
        line = '' 
        for ch in range(odd_num): 
                if ch % 2 == 0: 
                        line += '*'
                else: 
                        line += '*' 
        line = line.center(last, ' ') 
        print(line) 