# question3.py
# Author: Dominic Manthoko
# 24 March 2014

def frameUpp(f_thick,message):
    count = 0
    for i in range(f_thick,0,-1):
        print("|" * count+ "+" + ((len(message)+2*(i))*"-")+ "+"+ "|"*count )
        count +=1

def middle(repeat_count, message, f_thick):
    for i in range(0,repeat_count):
        print("|"*f_thick + " "+message + " " + "|"*f_thick)
        
        
def frameLower(f_thick,message):
    count2 = f_thick-1
    for x in range(1,f_thick+1):
        print("|" * count2+ "+" + ((len(message)+2*(x))*"-")+ "+"+ "|"*count2 )
        count2 -= 1
    
if __name__ == '__main__':
    message = input("Enter the message: \n")
    repeat_count = eval(input("Enter the message repeat count: \n"))
    f_thick = eval(input("Enter the frame thickness: \n"))    

    frameUpp(f_thick,message)
    middle(repeat_count, message, f_thick)
    frameLower(f_thick,message)