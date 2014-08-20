def print_square():
    
    print("*"*5)
    
    for i in range(3):
        print ("*"+" "*3+"*")
        
    print("*"*5)



def print_rectangle(width, height):
    
    print("*"*width)
    
    for i in range(height-2):
        print ("*"+" "*(width-2)+"*")
        
    print("*"*width)
    


def get_rectangle(width, height):
    
    
    Result = "*" * width+"\n"
    
        
    for i in range(height-2):
        i = "*"+" "*(width-2)+"*"
        
        Result += i
        Result += "\n"
        

    Result += "*" * width
    
    return Result
 



if __name__ == "__main__" :
    
    choice = str.lower(input("Choose test:\n"))
    choice = choice.split()
    
    if choice[0] == "a" :
        print_square()
        
    elif choice[0] == "b" :
        print("calling function")
        print_rectangle(int(choice[1]), int(choice[2]))
        print("called function")
        
    elif choice[0] == "c" :
        print("calling function")
        print("called function")
        print(get_rectangle(int(choice[1]), int(choice[2])))
    
    