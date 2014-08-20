def print_square():
        for i in range(1,6):
                
                if i==2:
                        print("*"," ","*")
                elif i==3:
                        print("*"," ","*")
                elif i==4:
                        print("*"," ","*")
                
                else :
                        print("*"*5)
                


def print_rectangle(width, height):
        x=width
        for i in range(1,height+1):
                
                if i ==1 :
                        print("*"*x)
                elif i == height :
                        print("*"*x)
                
                else  :
                        print("*"," "*(x-2),"*",sep="")


def get_rectangle(width, height):
    figure = ("*"* width+"\n")    
    for i in range(height-2):
        i = "*"+" "*(width-2)+"*"
        
        figure += i
        figure += ("\n")
        

    figure += "*" * width
    
    return figure
 



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
    
    
 