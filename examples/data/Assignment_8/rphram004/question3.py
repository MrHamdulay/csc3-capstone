x = input("Enter a message:\n")
def encrypt(x,z,y):
    if len(x) == len(z):
        print("Encrypted message:")        
        print(z)
        return
    
    if x == x.lower():
        step = x[y]
        #if step in range(97,122):
        if(ord(step)+1 in range(98, 123)):
            temp = chr(ord(step)+1)
            z += temp
        elif 122 == ord(step):
            z+="a"
        else:
            z+=step
        
            
        y += 1       
        encrypt(x,z,y)
        return
    else:
        print("Encrypted message:") 
        print(x)

encrypt(x,"",0)