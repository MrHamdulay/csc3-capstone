x= input("Enter the message:\n")
y = eval(input("Enter the message repeat count:\n"))
z = eval(input("Enter the frame thickness:\n"))

for i in range (0,(z+y)):
            if ((z-1) < i <(y+z)):
                        print(z*"|",x,z*"|")
                        
                                    
                                    
            else:
                        print((i*'|') + "+" + "-"*(len(x)+2+(z-1)*2 - i*2)+"+"+(i*"|"))

                                    
                                    
                                    
                                    
for p in range((z-1),-1,-1):
                                                
            if (p==0):
                        print("+" + "-"*(len(x)+2 + (z-1)*2 - p*2) + "+")
                                                            
            else:
                        print(p*'|' + "+" + "-"*(len(x)+2 + (z-1)*2 - p*2) + "+" + p*"|")
                                                            
            
            
                        
            

