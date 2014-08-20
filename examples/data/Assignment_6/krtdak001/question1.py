#KRTDAK001

def right():
    end = False
    myList = []
    userinput = input("Enter strings (end with DONE):\n")
    while end != True:    
        myList.append(userinput)
        userinput = input()
        if userinput == "DONE":
            end = True
    a = (len(max(myList, key=len)))
    i = 0
    print("\nRight-aligned list:")
    while i < len(myList):
        print((a - len(myList[i]))*" " + myList[i])
        i += 1
right()