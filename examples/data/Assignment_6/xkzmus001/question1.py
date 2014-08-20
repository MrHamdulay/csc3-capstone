"""question1.py
Author : Musa Xakaza
Date : 19/04/2014"""

names = []

def main():
    lenght , i = 0 , 0
    
    #get a list of strings & terminate when "DONE" is entered.
    #Get the length of the longest string.    
    name = input("Enter strings (end with DONE):\n")
    while name != "DONE":
        names.append(name)
        name = input()
        if len(names[i]) > lenght:
                    lenght = len(names[i])
        i += 1
                    
    #print the list of strings right-aligned with the longest string
    print("\nRight-aligned list:")
    for i in range(len(names)):
        out = "{0: >"+str(lenght)+"}"
        print(out.format(names[i]))
    
main()