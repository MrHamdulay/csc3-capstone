#frame message
#17 march 2014
#b harrilal

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

msgLen = len(message)
high= msgLen+ (2*thickness)
count=1

for m in range (0, thickness,1):
            if (count>1):
                        for n in range (1,count, 1):
                                    print("|",end="")
            print ("+",end="")
            for l in range (0, high):
                        print ("-",end="")
            print ("+",end="")  
            if (count>1):
                        for n in range (1,count, 1):
                                    print("|",end="")
            print()
            high = high -2
            count = count+1
                

for k in range (0, repeat, 1):
            for n in range (0,thickness, 1):
                                    print("|",end="")
            print (" ",end="")
            print (message,end=" ")
            for n in range (0,thickness, 1):
                                    print("|",end="")
            print()

high=high+2
count=thickness

for m in range (thickness, 0,-1): 
            if (count>1):
                        for n in range (1,count, 1):
                                    print("|",end="")
            print ("+",end="")
            for l in range (0, high):
                        print ("-",end="")
                        
            print ("+",end="")  
            if (count>1):
                        for n in range (1,count, 1):
                                    print("|",end="")
            print()
            high=high+2
            count = count-1
