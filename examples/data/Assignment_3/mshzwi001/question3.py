def main():
    message=input("Enter the message:\n")
    number=eval(input("Enter the message repeat count:\n"))
    thicknes=eval(input("Enter the frame thickness:\n"))
    mes=len(message)
    gap=thicknes
    count=0
    if mes>0:
        for i in range(thicknes):
            print("|"*count,"+-","-"*gap,"-"*(mes+gap-2),"-+","|"*count,sep="")
            gap=gap-1
            count+=1
        for i in range(number):
            print("|"*count," ",message," ","|"*count,sep="")
        for i in range(thicknes): 
            print("|"*(count-1),"+-","-"*gap,"-"*(mes+gap),"-+","|"*(count-1),sep="")
            gap=gap+1
            count-=1        
        
main()
