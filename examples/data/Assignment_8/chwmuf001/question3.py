
def pairs(mes):
    
    if mes.islower():
        if len(mes) == 0:
            print(mes)
        else:
            if mes[0] in " .?!" :
                
                print(mes[0], end = "")
                pairs(mes[1:])
            elif mes[0] == "z":
                print(chr(ord(mes[0])-25), end = "" )
                pairs(mes[1:])
            else:
                print(chr(ord(mes[0]) + 1), end = "")
                pairs(mes[1:])
            
    else:
        print(mes)
            
mes = input("Enter a message:\n")
print("Encrypted message:")
pairs(mes)