

x = input("Enter the message:\n")

y = eval(input("Enter the message repeat count:\n"))

z = eval(input("Enter the frame thickness:\n"))
b = len(x)

line=0
minuses=z+len(x)+z
for i in range(z):
        print("|"*(line)+"+"+"-"*(minuses)+"+"+"|"*line)
        minuses-=2
        line+=1

for i in range(y):
        print("|"*z+" "+x+" "+"|"*z)
        
line=z-1
minuses=2+len(x)
for i in range(z):
        print("|"*(line)+"+"+"-"*(minuses)+"+"+"|"*line)
        minuses+=2
        line-=1
  





#Previous attemps that did not workn out
#for i in range(1,z):
    
    #print("|"*i+"+-"+"-"*(b)+"-+"+"|"*i)
    #z-=2
#for i in range(y):
 #   z=2
  #  print("|"*z,x,"|"*z)
   
#for i in range(1,z):
 #   print("|"*i+"+-"+"-"*(b)+"-+"+"|"*i)
  #  z-=2
#print("+"+"-"*z+"-"*(b+4)+"-"*z+"+")
    
