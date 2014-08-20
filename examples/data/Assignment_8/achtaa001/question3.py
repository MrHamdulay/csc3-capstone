#Tahairah Achmat
def pair(m):
    
    if m.islower():
        if len(m) == 0:
            print(m)
        else:
            if m[0] in " .?!" :
                
                print(m[0], end = "")
                pair(m[1:])
            elif m[0] == "z":
                print(chr(ord(m[0])-25), end = "" )
                pair(m[1:])
            else:
                print(chr(ord(m[0]) + 1), end = "")
                pair(m[1:])
            
    else:
        print(m)
            
m = input("Enter a message:\n") #users input
print("Encrypted message:")
pair(m)