def main():
    x=[]
    y=input("Enter strings (end with DONE):\n")
    while y != "DONE":
        x.append(y)                            
        y=input("")
        if y=="DONE":                           
            count=0                            
            for i in range(0,len(x),1):
                z=len(x[i])
                if z >=count:
                    count=z
    print()
    print("Right-aligned list:")                
    for i in range(0,len(x),1):
        y=count-len(x[i])
        print(y*" "+x[i])                       
main()