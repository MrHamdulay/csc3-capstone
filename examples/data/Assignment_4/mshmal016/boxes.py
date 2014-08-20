y=5
def print_square(y):
    #for i in (lenth):
        print("*"*y)
        hol=y-2
        for i in range(y-2):
                print("*"," "*hol, "*",sep="")
        print("*"*y)
        return

        
#rectangle

def print_rectangle(w,h):
        print("*"*w)
        n=h-2
        for i in range(n):
                print("*", " "*(w-2), "*",sep="")
        print("*"*w)
        return
#if a=="b":
        #print("calling function")
        #print_rectangle(5,4)  
        #print("called function")
        

def get_rectangle(w,h):
        print("called function")
        print("*"*w)
        for i in range(h-2):
                print("*", " "*(w-2),"*",sep="")
        print("*"*w)
        return        

t=input("Choose test:\n")

if t=="a":
        print_square(y)
else:
        w=eval(input())
        h=eval(input())
        print("Calling function")
        
        if t=="b":
                print_rectangle(w,h)
                print("called function")

        elif t=="c":
                #print("called function")
                get_rectangle(w,h)