# Assignment 6
# Program to take entered names and right-aligh them
# Frans van Hoek   
# 22 April 2014

def get_names():
    list_n = []
    print("Enter strings (end with DONE):")
    while True:
        name = input("")
        if name == 'DONE':
            break
        else:
            list_n.append(name)
    return list_n

def align_names(list_n):

    # First find the longest string
    maxlength = 0
    for i in list_n:
        if len(i) > maxlength:
            maxlength = len(i)
    
    # Then print the names        
    print("\nRight-aligned list:")
    for i in list_n:
        space = maxlength - len(i)
        print(space*' ' + i)
        
x = get_names()
align_names(x)