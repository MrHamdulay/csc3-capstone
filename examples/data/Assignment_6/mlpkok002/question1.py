def right_alignment():
    
    strings=[] #create empty list
    string=input("Enter strings (end with DONE):\n") #prompt user for strings
    if string!="DONE":    #if the first string is not DONE
        while string!="DONE":   
            strings.append(string) #keep filling list until user enters DONE
            string=input("") #alternative to: enter strings (end with DONE)
            
        print("")
        print("Right-aligned list:")
        maxlength = max(len(string) for string in strings) #get the length of the longest string
        for string in strings:
            gap=maxlength-len(string) #create variable gap, which changes according to the length of each. String with the longest lenghth will have no gaps before it
            print(" "*gap+string)
    else:  #if the first string is DONE
        print(" ")
        print("Right-aligned list:")
        print(" ")

right_alignment()
