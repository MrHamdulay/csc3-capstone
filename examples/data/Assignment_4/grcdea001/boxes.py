def print_square():
        print("*****")
        for i in range(3):
                print("*","*",sep = "   ")
                
        print("*****")

def print_rectangle(x,y):
        print("*"*x)
        for i in range(y-2):
                print("*","*",sep = " "*(x-2))
        print("*"*x)
        
def get_rectangle(x,y):
        toreturn =("*"*x)
        for i in range(y-2):
                toreturn = toreturn + "\n*" +" "*(x-2)+"*"
        toreturn = toreturn + "\n" + ("*"*x) 
        return toreturn

                
        