def main():
    print("Independent Electoral Commission")
    print("--------------------------------")
    print("Enter the names of parties (terminated by DONE):")
    x=[]
    y=""
    z=[]
    a=0
    while y!="DONE":
        y=input("")
        
        if y!=("DONE"):
            z.append(y)
            
    for i in range(len(z)):
            
        if z[i] in x:
                a=a+1
                
        else:
            x.append(z[i])
                
    x.sort()
    print("\nVote counts:")

    for j in range(len(x)):
        print((x[j]),(9-len(x[j]))*" ","-",z.count(x[j]))
            
main()