#HLNSIB005: Sibulele Hlongwane
message= input("Enter the message:\n")
count= eval(input("Enter the message repeat count:\n"))
thickness= eval(input("Enter the frame thickness:\n"))
length= len(message)
icount=0

for i in range(thickness,0,-1):
    print("|"*icount,"+",("-"*length),(2*(i)*"-"), "+","|"*icount, sep="")
    icount=icount+1

for i in range(count):
    print("|"*thickness,message,"|"*thickness)

icount=thickness-1    

for i in range(thickness):
    print("|"*icount,"+",("-"*length),(2*(i+1)*"-"), "+","|"*icount, sep="")
    icount=(icount-1)

          
          
          
          
          
          #pattern
          # word=11
          # 13:1   added by 2
          # 15:2   added by 4
          # 17:3   added by 6