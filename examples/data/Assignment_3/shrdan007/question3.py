# Assignment 3, question 3
# Danielle Sher
# 19 March 2014

def enter_info():
    x = x_message = input("Enter the message:\n")
    y = y_repeat = eval(input("Enter the message repeat count:\n"))
    z = z_thickness = eval(input("Enter the frame thickness:\n"))
    
    for i in range(z):
        print("|"*i + "+" + ("-" * (len(x) + 2*z  - 2*i) + "+" + i*"|"))
                
    for i in range(y):
        print("|"* z + " " + x + " " + "|" * z)   
        
    for i in range(z):
        print("|"*(z - i - 1) + "+" + ("-" * (len(x) + 2*(i)+2)) + "+" + "|"*(z - i - 1))
                    

enter_info()







