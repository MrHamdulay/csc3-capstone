# Kieran Reilly, RLLKIE001
# Working with functions: Printing a box;
# 31/03/14

def print_square():
    size = 5
    star = "*"
    
    print(star*size)
    for i in range(size-2):
        print(star+" "*(size-2)+star)
    
    print(star*size)
    
    
def print_rectangle(x,y):
    width = x
    height = y
    star = "*"
    
    print(star*width)
    for i in range(height - 2):
        print(star+" "*(width-2)+star)
    
    print(star*width)
    
    
    
def get_rectangle(x,y):
    width = x
    height = y
    
    print_rectangle(width,height)    
    
    
if __name__ == "__main__":
    
    choice = input("choose a test: \n")
    
    if choice[0] == "a":
        print_square()
    
    if choice[0] == "b":
        print("calling function")
        x = int(choice[2])
        y = int(choice[4])
        
        print_rectangle(x,y)
        print("called function")
        
    if choice[0] == "c":
        print("calling function")
        print("called function")
        x = int(choice[2])
        y = int(choice[4])
                
        get_rectangle(x,y)        
        