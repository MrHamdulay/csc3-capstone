#Assignment 3, Question 3
#Author: Sabir Buxsoo
#Class: CSC1015F 2014
#Date Created: 27/03/2014; Updated: 28/03/2014

#This program is used to create a frame with a defined thickness which wraps a message of specified repetition.

#Defining the function frame() to create the frame with the message.
def frame():
    #Pre-condition: Input message, message repeat count and frame thickness.
    #Post-condition: Generate frame with message.
    
    #Input Variables
    message = input("Enter the message:\n")
    repeat = eval(input("Enter the message repeat count:\n"))
    thickness = eval(input("Enter the frame thickness:\n"))
    
    
    #Defining variables to make the frame.
    message = " " + message + " " #Updates the message adding a space before and after.
    plus = "+" #Defining + as a variable for simplicity.
    dash = "-" * len(message) #This generates the minimum number of dash needed(i.e dash for the line just before the message).
    dashUpdater = thickness - 1
    barUpdater = 0 #Initializing value of | set to 0 for the first line.
    bar = "|" * barUpdater #Defines number of |, which is 0 initially. 
    
    #Creating the Upper part of the frame.
    #Pre-condition: Create the first line, using only plus and dash, since bar == 0.
    #Post-condition: Update | and the number of - and create the second line. Repeat for range of specified thickness.
    for upperFrame in range(thickness):
        newLine = bar + plus + dash + ("-" * (dashUpdater*2)) + plus + bar 
        print(newLine)
        barUpdater = barUpdater + 1
        dashUpdater = dashUpdater -1
        bar = "|" * barUpdater
    
    #Creating the middle part of the frame.
    for middleFrame in range(repeat):
        print ("|"*(thickness) + message + "|"*(thickness)) #Print message "repeat" number of times.
       
    #Resetting frame Variables.
    dashUpdater = 0
    barUpdater = thickness - 1
    bar = "|" * barUpdater
    
    #Creating the Lower part of the frame.
    #Pre-condition: Bar is set to max, dash is set to min and first line is created.
    #Post-condition: Update | and the number of - in reverse order compared to Upper part of Frame and create another line. Repeat for range of specified thickness.
    for lowerFrame in range(thickness):
        newLine = bar + plus + dash + ("-" * (dashUpdater*2)) + plus + bar 
        print(newLine)
        barUpdater = barUpdater - 1
        dashUpdater = dashUpdater +1
        bar = "|" * barUpdater    
        
frame()