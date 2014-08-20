hgt = int(input("Enter the height of the triangle:\n"))
for i in range(hgt):
    
    print((' ' * ( hgt - i - 1 ) + '*' * ( 2 * i + 1)))
