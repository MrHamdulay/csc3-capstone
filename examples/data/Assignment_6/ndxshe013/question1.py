def main():
    inp = ""
    name = []
    no = 0;
    print("Enter strings (end with DONE):\n")
    while (inp!="DONE"):
        inp = input();
        name.append(inp)
        how = len(inp)

        if (how > no):
            no = how
    print("Right-aligned list:")             
    for i in range(len(name)-1):
        x = len(name[i])
        y = no - x
        print(" "*(y)+name[i])
 
main()
    
