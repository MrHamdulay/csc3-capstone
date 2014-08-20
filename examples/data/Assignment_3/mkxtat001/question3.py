#Tato Moaki MKXTAT001
#Program to draw a frame around a message user input
#question3 Assignment3
def main():
    str1 = input("Enter the message:\n")
    count = eval(input("Enter the message repeat count:\n"))
    n = eval(input("Enter the frame thickness:\n"))
    
    j = 2 * n
    k = 2
    
    for i in range(0,n):
        print("|"*i,"+","-"*(len(str1)+(j)),"+","|"*i,sep="")
        j -= 2
        
    for l in range(0,count):
        print("|"*n," ",str1," ","|"*n,sep="") 
        
    for i in range(n-1,-1,-1):
        print("|"*i,"+","-"*(len(str1)+(k)),"+","|"*i,sep="")
        k += 2    

main()
