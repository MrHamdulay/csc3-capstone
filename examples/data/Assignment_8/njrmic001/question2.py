#A program to count the number of pairs of adjacent repeated characters in a string
#Author: Michelle Njoroge
#10 May 2014

message=input("Enter a message:\n")
count=0
def repeat(message):
    global count
    if len(message)<2:
        print("Number of pairs:", count)
    elif len(message)>=2:
        if message[0]==message[1]:
            count+=1
            return repeat(message[2:])
        elif message[0]!=message[1]:
            return repeat(message[1:])

repeat(message)

        
        
        