 n=input("Enter a message:\n")
def pairs(n):
    
    
    if n=="":
        return n
    if len(n)==0:
        return 0
    elif n[0]==" ":
        return pairs(n[1:])
    elif n[0]==n[1]:
        return 1+ pairs(n[2:])
    else:
        return pairs(n[1:])
print("Number of pairs:",pairs(n))       
