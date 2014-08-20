"""Program to align names
Sbonelo Mntungwa
25 April 2014"""

def main():
    #Making the list
    name = input("Enter strings (end with DONE):\n")
    list_of_names = [name]
    while name!="DONE":
        name = input("")
        if name != "DONE":
            list_of_names.append(name)
        else:
            break
    print(' ')
    #Determining the maximum length in the list
    max_length = max(len(i) for i in list_of_names)
    #Adjusting the alignment
    print("Right-aligned list:")
    for i in list_of_names:
        print(i.rjust(max_length))       
        
        
main()
