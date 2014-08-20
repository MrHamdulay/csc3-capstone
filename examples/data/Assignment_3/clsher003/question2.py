
x = int(input("Enter the height of the triangle:\n"))
last_line = (x * 2) - 1
for odd_num in range(1, last_line+1, 2):
        line = '*' * odd_num
        line = line.center(last_line, ' ')
        print(line)
        