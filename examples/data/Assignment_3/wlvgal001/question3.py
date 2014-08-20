#message
message=" "+input("Enter the message:\n")+" "
repeat=eval(input("Enter the message repeat count:\n"))
thick=eval(input("Enter the frame thickness:\n"))

for i in range(0,thick,1):
            print(i*"|",end='')
            for l in range(0,thick):
                        print("+",((len(message)+(thick-1)*2-(2*i))*'-'),'+',sep='',end='')
                        break
            print(i*"|")  
for j in range(repeat):
            print(thick*"|",end='')
            print(message,end='')
            print(thick*"|")
for i in range(thick-1,-1,-1):
            print(i*"|",end='')
            for l in range(len(message),len(message)+thick , 2):
                        print("+",((len(message)+(thick-1)*2-(2*i))*'-'),'+',sep='',end='')
                        break
            print(i*"|")  

            
      


