#border 
#Tofunmi Olagoke
#OLGMOF001

#overall assignment
message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))
num=len(message)

#function 1
f1_1=num+2 
f1_2=(thick-1)*2+f1_1
f1_3=0

while f1_2>= f1_1 and f1_3<thick: 
    print("|"*f1_3+"+"+f1_2*"-"+"+"+"|"*f1_3)
    f1_2=f1_2-2
    f1_3=f1_3+1

#function2
f2_1=(f1_1-num)//2
           
for a in range(repeat):
    print("|"*thick+" "*f2_1+message+" "*f2_1+"|"*thick)

#function 3
f3_1=thick-1
f3_2=f1_1
f3_3=thick-1

while f1_1+2*thick>f3_2>=f1_1: 
    print("|"*f3_3+"+"+f3_2*"-"+"+"+"|"*f3_3)
    f3_1=f3_1-1
    f3_2=f3_2+2
    f3_3=f3_3-1