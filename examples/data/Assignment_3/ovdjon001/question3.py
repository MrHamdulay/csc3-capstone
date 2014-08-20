def main():
    word = input("Enter the message:\n")
    wordRep = eval(input("Enter the message repeat count:\n"))
    frameThickness = eval(input("Enter the frame thickness:\n"))
    #print top part
    for i in range(0,frameThickness):
        line ="|"*i + "+" +"-"*(len(word)+frameThickness*2-i*2) +"+" + "|"*i
        print(line)
        
    #print the middle part    
    for i in range(0,wordRep):
        line = "|"*frameThickness +" " +word+" " +"|"*frameThickness
        print(line)
    #print last part 
    for i in range(frameThickness-1,-1,-1):
        line ="|"*i + "+" +"-"*(len(word)+frameThickness*2-i*2) +"+" + "|"*i
        print(line)
main()