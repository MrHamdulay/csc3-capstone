#code to ask user for input
message= input("Enter the message:\n")
message_count= int(input("Enter the message repeat count:\n"))
thick= int(input("Enter the frame thickness:\n"))
characters= len(message) #number of characters in message

plus = "+"
minus="-"
hush="|"
mess="|"*thick+" "+ message+" "+"|"*thick
count= len(mess)
i = 0
hush_count=0
#code to print top boundary
for i in range(0,thick):
    print(hush*i+"+"+minus*(count-((2*i)+2))+"+"+hush*i)
j=i
#code to print message body
for i in range(0,message_count):
    print(mess)
    i=i+1
#code to print lower boundary    
i=thick
while(i>0):
    print(hush*j+"+"+minus*(count-((2*j)+2))+"+"+hush*j)
    j=j-1
    i=i-1
    
