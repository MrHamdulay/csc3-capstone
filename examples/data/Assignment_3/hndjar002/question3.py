# 24 March 2014
# Jaren Hendricks
# Program to print a frame around a message

def main():
    message = input("Enter the message:\n")
    count = eval(input("Enter the message repeat count:\n"))
    frame = eval(input("Enter the frame thickness:\n"))

    message = " "+message+" " 
    lentop= len(message)
    lenbottom= len(message)
    border = 2    

    for top in range(frame): 
        calc = frame-top-1
        print(top * "|"+"+"+ "-" * int((lentop)+2 * calc) +"+" + "|" *top)

    for i in range(count):
        print("|"*frame +message+ "|"*frame)

    for bottom in range(frame, 0, -1):
        print(int(bottom-1) * "|" +"+"+ str(lenbottom * "-") +"+"+ str("|"*int(bottom-1)))  
        lenbottom += border
main()
    
    
