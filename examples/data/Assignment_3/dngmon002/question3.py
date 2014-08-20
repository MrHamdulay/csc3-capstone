# Making a frame with a word in it
# Monwabisi Dingane
# 24 March 2014

def frameBuild(repeat,thickness,word):
    
    for i in range(0,((thickness*2)+2)+len(word)):
        
        if i == 0 or i == (((thickness*2)+2)+len(word)-1):
            print("+",end='')
        else:
            print("-",end='')
            
    print()        
    
    for j in range(0,((thickness*2)+2)+len(word)):
        
        if j == 0 or j == (((thickness*2)+2)+len(word)-1):
            print("|",end='')
        
        elif j == 1 or j == (((thickness*2)+2)+len(word)-2):
            print("+",end='')
        
        else:
            print("-",end='')  
    
    print()
    
    k = 0
    while k != repeat:
        print("|"*thickness,word,"|"*thickness)
        k += 1
        
    for i in range(0,((thickness*2)+2)+len(word)):
        
            if i == 0 or i == (((thickness*2)+2)+len(word)-1):
                print("|",end='')
                
            elif i == 1 or i == (((thickness*2)+2)+len(word)-2):
                print("+",end='')
                
            else:
                print("-",end='')            
                
    print()        
        
    for j in range(0,(((thickness*2)+2)+len(word))):
        
        if j == 0 or j == (((thickness*2)+2)+len(word)-1):
            print("+",end='')

        else:
            print("-",end='')     

w = input("Enter the message:\n")
r = eval(input("Enter the message repeat count:\n"))
t = eval(input("Enter the frame thickness:\n"))

frameBuild(r,t,w)