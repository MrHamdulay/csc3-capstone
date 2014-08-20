#FrameZ
message = input("Enter the message:\n")

repeat = eval(input("Enter the message repeat count:\n"))

thick = eval(input("Enter the frame thickness:\n"))

for Tops in range (0,(repeat+thick)):
            
            if ((thick-1) < Tops <( thick + repeat)):
                        print("|"*thick,message,"|"*thick)
                        
            else:
                        print('|'*Tops + "+" + "-"*(len(message)+2 + (thick-1)*2 - Tops*2) + "+" + "|"*Tops)

for Bottom in range((thick-1),-1,-1):
            
            if (Bottom==0):
                        print("+" + "-"*(len(message)+2 + (thick-1)*2 - Bottom*2) + "+")
                        
            else:
                        print('|'*Bottom + "+" + "-"*(len(message)+2 + (thick-1)*2 - Bottom*2) + "+" + "|"*Bottom)
                        