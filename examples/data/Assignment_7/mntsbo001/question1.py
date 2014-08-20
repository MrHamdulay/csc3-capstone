"""Creating unique list
Sbonelo Mntungwa
2 May 2014"""



def main():
    list = [] #making list
    string = input("Enter strings (end with DONE):\n") #inputing string
    while string!= "DONE": #terminating the input with DONE
        if string not in list: #avoiding duplicates
            list.append(string) #adding to list
        string = input("")
    print()   
    print("Unique list:")
    for i in list:#printing the new list
        print(i)
main()
    