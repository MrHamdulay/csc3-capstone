#Q1 of Assignment 3
#KVRSHA004
#Framed message

message = input("Enter the message: \n")
count = eval(input("Enter the message repeat count: \n"))
frame = eval(input("Enter the frame thickness: \n"))

endline = 0
hyphens = 2*frame

for i in range(frame):
    print("|"*endline, "+", "-"*(len(message)+hyphens), 
          "+", "|"*endline, sep="")
    endline+=1
    hyphens-=2
    
for i in range(count):
    print("|"*frame, message, "|"*frame)
    
endline-=1
hyphens+=2
    
for i in range(frame):
    print("|"*endline, "+", "-"*(len(message)+hyphens), 
          "+", "|"*endline, sep="")
    endline-=1
    hyphens+=2