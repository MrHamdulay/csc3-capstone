#Athour:Percival Munhuwaani
#Program:Printing strings in the same order without duplicates
#Date:01/05/2014
def main():
    string=input("Enter strings (end with DONE):\n")
    string_list=[]#empty list to store the strings
    string_dict={}#empty dictionary to store the strings as keys
    while string!="DONE":
        if string not in string_dict:
            string_dict[string]=1
            string_list.append(string)#adding the strings to the list
        string=input()
    print()
    print("Unique list:")
    for string in string_list:#iterating the list of strings
        print(string)
main()

