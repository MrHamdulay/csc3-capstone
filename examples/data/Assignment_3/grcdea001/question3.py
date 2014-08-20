# Dean Gracey, GRCDEA001, assignment 3 question 1
message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

downs = 0
dash = thickness
for i in range (0,thickness):
    
    print("|"*downs,"+","-"*dash,"-"*len(message),"-"*dash,"+","|"*downs,sep = "")
    downs+=1
    dash-=1

for i in range(0,repeat):
    print("|"*thickness, message, "|"*thickness, sep = " ",)
    

downs = thickness-1
dash = 1 
for i in range (0,thickness):
        
    print("|"*downs,"+","-"*dash,"-"*len(message),"-"*dash,"+","|"*downs,sep = "")
    downs-=1
    dash+=1