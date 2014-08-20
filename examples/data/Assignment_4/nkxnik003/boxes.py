#Nikhil Jiten Naik 
#NKXNIK003

def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(x,y):
    print("*"*x)
    for i in range(y-2):
        print("*"+" "*(x-2)+"*")
    print("*"*x)
def get_rectangle(a,b):
    end = "*"*a+"\n" 
    for i in range(b-2):
        end+=("*"+" "*(a-2)+"*"+"\n")
    end+= "*"*a
    return end
    