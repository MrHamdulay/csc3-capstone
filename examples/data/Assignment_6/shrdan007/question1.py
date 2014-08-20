# Program to right-align a list
# Danielle Sher


strlist = []
x = input("Enter strings (end with DONE):\n")
if x != "DONE":
    while True:
        if x != "DONE":
            strlist.append(x)
            x = input("")
        elif x == "DONE":
            break

    y = strlist
    width = (max(map(len, y)))

    print()
    print ("Right-aligned list:")
    for i in y:
        print (" "*(width - len(i)) + i)
   
elif x == "DONE":
    print()
    print("Right-aligned list:")
    



   
        
        
    



