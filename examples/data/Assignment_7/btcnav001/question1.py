

def main():


    print("Enter strings (end with DONE):")
    x = input()
    y = []
    while x != "DONE":
        y.append(x)
        x = input()
    
    

    z = []
    for i in y:
        if i not in z:
            z.append(i)
            
            

    print("\nUnique list:")
    for i in z:
        print(i)
        
if __name__=="__main__":
    main()