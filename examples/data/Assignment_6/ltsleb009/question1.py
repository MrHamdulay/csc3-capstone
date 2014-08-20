#-------------------------------------------------------------------------------
# Name:        QUESTION1
# Purpose:      ASSIGNMENT 6
#
# Author:      Taylor
#
# Created:     23/04/2014
# Copyright:   (c) Taylor 2014
#-------------------------------------------------------------------------------

def main():
    """prints out a list of strings right-aligned with the longest string"""

    max_len = 0
    string = input("Enter strings (end with DONE):\n")
    data  = [] #create an empty list

    if string == "DONE":
         print("\nRight-aligned list:")
    else:

        data.append(string) #add string to list
        max_len = len(string)

        while True:

            string = input()

            if not string == "DONE": #repeat this 'til string value is "DONE"

                if len(string) > max_len:
                    max_len = len(string) #check if length of current string is greater
                data.append(string) #add new string to list
                continue

            break

        print("\nRight-aligned list:")

        for word in data: #iterate over the list one word at a time

            tab = max_len  - len(word) #determine justification of word
            print(tab*" "+(word))

if __name__ == '__main__':

    main()
