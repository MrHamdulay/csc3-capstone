"""This function takes strings given by the user  followed by the sentinel "DONE" and the list of strings is then printed out right-aligned with the longest string.
Mtunzi France
24 April 2014"""

"""Ask the user to enter a string"""
def question1():
    myList = []
    strings = input("Enter strings (end with DONE):\n")
    myList.append(strings) #adds the input into the empty list
    if myList[0] == "DONE":
        print("")
        print("Right-aligned list:\n")
    else:
        """Continues asking for more strings until DONE is entered."""
        while "DONE" not in myList:
            moreStrings = input()
            myList.append(moreStrings)
        myList.remove("DONE") #removes DONE from list
        """Tries to find the word with maximum length in a list"""
        Max = len(myList[0])
        for i in range(0,len(myList)):
            if len(myList[i]) > Max:
                Max = len(myList[i])
            if len(myList[i]) <= Max:
                Max = Max
        print("")
        """Aligns the strings to the right"""
        print("Right-aligned list:")
        for i in myList:
            print(i.rjust(Max))
        
question1()