#Keanon Fell
#1 April 2014
#

def print_square():
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")
    
def print_rectangle(w,h):
    print("calling function")
    for i in range(0,h):
        if i == 0 or i==h-1:
            print("*"*w)
        else:
            print("*" + " "*(w-2) + "*" )
    print("called function")
            
def get_rectangle():
    print("calling function") 
    
#====================================================================
    
answer = input("Choose test:\n")
    
if answer[0] =='a':
    print_square()
elif answer[0] == 'b':
    print_rectangle(eval(answer[2]),eval(answer[4]))
elif answer[0] == 'c':
    get_rectangle()    