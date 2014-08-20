def main():
    message=input("Enter the message:\n")
    repeat= eval(input("Enter the message repeat count:\n"))
    thick= eval(input("Enter the frame thickness:\n"))
    
    length= len(message)+(2*thick) 
    line= 0
    for i in range(thick):
        print("|"*line,"+","-"*length,"+","|"*line,sep="")
        line+=1
        length-=2
        
    for i in range(repeat):
        print("|"*thick," ",message," ","|"*thick,sep="")
        
    length2= len(message)+2
    line= thick-1
    for i in range(thick):
        print("|"*line,"+","-"*length2,"+","|"*line,sep="")
        line-=1
        length2+=2

main()

            