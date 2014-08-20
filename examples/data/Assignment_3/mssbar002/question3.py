# Assignment 3. Question 3
# a program to draw a frame (made of the characters +-|) around a message
# that has been repeated on consecutive lines.  
# There is a space before and after the message, and no spaces between concentric boxes.

# Author: Barnett msiska(MSSBAR002)
# Date: 22/03/2014

def main():
    # request user input
    message = input("Enter the message:\n")
    repeatCount = eval(input("Enter the message repeat count:\n"))
    frameThickness = eval(input("Enter the frame thickness:\n"))
    
    # process frame
    
    #frameTop = '|+' + '{0}' + '+|'
    frameTop = '{0}' + '{1}' + '{2}' + '{3}' + '{4}'

    #middle = '|| ' + message + ' ||'
    middle = '{0}' + ' ' + message + ' ' + '{1}'
    
    #frameBottom = '|+' + '{0}' + '+|'    
    frameBottom = '{0}' + '{1}' + '{2}' + '{3}' + '{4}' 
    
    if repeatCount > 0 and frameThickness > 0:
        # print frame
        # Top
        t = frameThickness 
        print(frameTop.format('|' * (frameThickness - t), '+', '-' * (len(message) + t*2), '+' , '|' * (frameThickness - t)))
        t -= 1
        while t > 0:
            print(frameTop.format('|' * (frameThickness - t), '+', '-' * (len(message) + t*2), '+' , '|' * (frameThickness - t)))
            t -= 1
        
        # middle
        while repeatCount > 0:
            print(middle.format('|' * frameThickness, '|' * frameThickness))
            repeatCount -= 1
        
        # bottom    
        t = frameThickness 
        centerIncriment = 1
        while t > 1:
            t -= 1
    
            print(frameTop.format('|' * (t), '+', '-' * (len(message) + 2*centerIncriment), '+' , '|' * (t)))
            centerIncriment += 1
               
        print(frameTop.format('|' * (0), '+', '-' * (len(message) + frameThickness*2), '+' , '|' * (0)))
        t -= 1

        
main()