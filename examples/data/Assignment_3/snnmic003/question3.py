# Question 3

sentence = input ("Enter the message:\n")
repeat = eval (input ("Enter the message repeat count:\n"))
frame = eval (input ("Enter the frame thickness:\n"))

height = (repeat + frame*2)
width = len(sentence) + (2 * frame)

for i in range (height):
    
    if (i < frame):
        if (i==0):
            print ("+" , end = "")
        if (i != 0):
            print ((i)*"|", end = "")
            print ("+", end = "")            

        for j in range (width):
            print ("-", end = "")

        if (i == 0):
            print("+")
        else:
            print ("+" + "|"*i)
        width -=2

    if (i >= (frame) and i < (frame+repeat)):
        print (frame * "|", end = "")
        print (" " + sentence + " " , end = "")
        print (frame * "|")
        
    if i >= (frame+repeat):
        width+=2
        if (i==(height - 1)):
            print ("+" , end = "")
        if (i != (height - 1)):
            print ((height - i - 1)*"|", end = "")
            print ("+", end = "")   
        for j in range (width):
            print ("-", end = "")
            
        if (i == (height-1)):
            print("+")
        else:
            print ("+" + "|"*(height-1 - i))     