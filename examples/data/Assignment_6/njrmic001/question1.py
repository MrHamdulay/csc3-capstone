#A program that asks the user for a list of strings and prints these out right aligned with the longest string
#Author: Michelle Njoroge
#23 April 2014

#define a function
def main():
    listnames=[]
    name=input("Enter strings (end with DONE):\n")
    while name!="DONE":
        listnames.append(name)
        name=input()
    width=0
    for string in listnames:
        if len(string)>width:
            width=len(string)
        else:
            width=width
    print()
    print("Right-aligned list:")
    for string in listnames:
        format_word=(" "*(width-len(string))+string)
        print(format_word)
main()        
