#program where the user can enter a list of strings
#Jenny Luo
#23 April 2014

def main():
    #add string into a list called strings
    strings=[""]
    string=input("Enter strings (end with DONE):\n")
    while string !="DONE":
        strings.append(string)
        string=input("")
    
    #get the length of the longest string
    Rightalign=0
    for i in range(len(strings)):
        if len(strings[i])>Rightalign:
            Rightalign=len(strings[i])
    print()
    print("Right-aligned list:", end="")
    
    #get the list of strings right justified
    for j in range(len(strings)):
        print(strings[j].rjust(Rightalign))
main()
                 
                 