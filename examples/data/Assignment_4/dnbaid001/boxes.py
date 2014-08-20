#Aidan de Nobrega
#Functions for creating boxes of varying sizes
#31/03/2104

# prints a 5 x 5 square
def print_square():
    print('*'*5) 
    print(('*   *'), ('*   *'), ('*   *'), sep = '\n') # prints 3 middle lines on separate lines
    print('*'*5)

# prints a w x h square    
def print_rectangle(w, h):
    print('*'*w) #prints * for each unit of width
    for i in range(h-2): # accounts for line on top and bottom
        print('*' + ' '*(w-2) + '*')
    print('*'*w)

# returns a w x h square as a string
def get_rectangle(w, h):
    rectangle = "" #string holder
    first_line = '*'*w
    middle = '*' + ' '*(w-2) + '*'
    rectangle += first_line + '\n'
    rectangle += (middle + '\n')*(h-2)
    rectangle += first_line
    return rectangle