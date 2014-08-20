#Kieran Reilly, RLLKIE001
#Right Justified list of strings
#Assignment6, question1
#21/04/14

inStrings = []
count = 0

tempString = input("Enter strings (end with DONE):\n")

#filling the list
if tempString == "DONE":
    print("Right-aligned list: ")
else:
    while tempString != "DONE":
        inStrings.append(tempString)
        tempString = input("")
        count += 1
    print("")
#getting length of longest string in list
    length = len(inStrings[0])

    for i in range(count):
        if(length < len(inStrings[i])):
            length = len(inStrings[i])

#printing right-justified
    out = "{0:>"+str(length)+"}"        #format string

    print("Right-aligned list: ") 
    for i in range(count):
        print(out.format(inStrings[i]))
    