def triprint(h):
    for i in range(1, h+1):
        print(('*'*(2*i-1)).center(2 * h - 1))
        
def triprint_2(h):
    for i in range(1, h + 1):
        spaces = (h - i) * ' '
        print(spaces + (2 * i-1)*'*')
        
if __name__ == '__main__':
    height = eval(input("Enter the height of the triangle:\n"))
    triprint_2(height)