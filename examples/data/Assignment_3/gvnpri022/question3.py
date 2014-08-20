msg = input("Enter the message:\n")
count= eval(input("Enter the message repeat count:\n"))
thick= eval(input("Enter the frame thickness:\n"))
l= len(msg)
h1="+"+(l+(2*thick))*"-"+"+"
lh1= len(h1)
h2= "|+"+(l+(1*thick))*"-"+"+|"
h2= h2.center(lh1)
lh2= len(h2)
msg1="|| "+ msg+ " ||"
for i in range(1,(count+(thick*2))+1):
    if(i==thick):
        endFactor=i
        midFactor=(l+(2*((thick-(i-1)))))
    if(1<=i<=thick):
        noLine= (i-1)*"|"
        print(noLine+"+"+(l+(2*((thick-(i-1)))))*"-"+"+"+noLine)
        
    elif(thick<=i<=(count+(thick*2)-thick)):
        print(thick*"|"+" "+msg+" "+ thick*"|")
        
    else:
        noLine= (endFactor-1)*"|"
        
        print(noLine+"+"+midFactor*"-"+"+"+noLine)  
        endFactor=endFactor-1
        midFactor=midFactor+2
        
   # if(i==1) or (i==(count+4)):
    #    print(h1)
    
   # elif(i==2) or (i==(count+3)):
      #  print(h2)
    
    #else:
       # print(msg1)