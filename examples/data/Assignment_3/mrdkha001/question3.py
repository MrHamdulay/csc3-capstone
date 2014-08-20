# Question 3

Message = input("Enter the message:\n") 
Repetition =eval(input("Enter the message repeat count:\n"))
Frame = eval(input("Enter the frame thickness:\n"))


def framedraw(a,b,c): 
        plus_1 = "+"
        plus_2 = "+"
        plus_3, plus_4 = "+","+"
        thickness = c
        maxthickness = c
        constant = 1
        for i in range(c, 0, -1):
                print(plus_1 + "-" * (len(a) + c * 2) + plus_2)
                c = c - 1
                if c >= 0:
                        plus_1 = "|" + plus_1  
                        plus_2 = plus_2 + "|"
        while b > 0:
                print("|" * thickness, a, "|" * thickness)
                if b == 1:                     
                        for i in range(0, thickness , 1):
                                print( ("|" * (thickness - 1) + plus_3) + ("-" * (len(a) + (constant * 2) )) + (plus_4 + ("|" * (thickness - 1))))
                                c = c + 2
                                thickness = thickness - 1
                                constant = constant + 1
                                plus_3 = plus_3.replace("|", "")
                                plus_4 = plus_4.replace("|","")
                                
                b = b - 1
               
framedraw(Message, Repetition, Frame)




