message=input("Enter the message:\n")
repeat=eval(input("Enter the message repeat count:\n"))
thickness=eval(input("Enter the frame thickness:\n"))

message2 = thickness * '|' +" "+ message +" "+ thickness *'|'

#print (message2)
dash=len(message2)-2
#print(dash)


for j in range ((thickness)):
    print(j* "|" + "+" ,end="")
    print("-" * dash +"+" + j*"|")
    dash=dash-2
    
for i in range (repeat):
    print(thickness*"|",message,thickness*"|")

m3 = thickness * '|'  
m=len(m3)-1

dash2=" "+ message +" "
d=len(dash2)

for k in range (m,0,-1):
        print(k* "|" + "+" ,end="")
        print("-" * d +"+" + k*"|")
        d=d+2

end=len(message2)-2

if(repeat>0 and thickness > 0):
    print("+" + end*"-" + "+")
    
 
    
    
    
