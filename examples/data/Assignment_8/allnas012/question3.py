def encode_rec(x):
    if x[0]==" ":
        return " "+encode_rec(x[1:])
    elif x[0]==x[len(x)-1]:        
        if x[0].islower():
            if x[0]=="z":                     
                return "a" 
            else:
                return chr(ord(x[0])+1)
        else:
            return x[0]
    elif x[0].islower():
        if x[0]=="z":                       
            return "a"+encode_rec(x[1:])       
        else:            
            return chr(ord(x[0])+1)+encode_rec(x[1:])
    elif x[0].isupper():
        return x[0]+encode_rec(x[1:])      
    else:
        return encode_rec(x[1:])

if __name__ == "__main__":  
    ans = input("Enter a message:\n")
    print("Encrypted message:")
    print(encode_rec(ans))