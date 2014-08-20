"""Removes duplicates from a list of strings
Paul Freund
01/05/14"""

def listmaker_nodup(): 
    """creates the string list needed by asking for input strings and adding them to list no duplicates found"""
    string_list = []
    string = ""
    while string != "DONE":
        string = input()
        if string != "DONE":
            if string not in string_list:
                string_list.append(string)
    return string_list

def main():
    """prints out input instructions, runs listmaker_nodup and prints out the needed output"""
    print("Enter strings (end with DONE):\n")
    _list = listmaker_nodup()
    print("Unique list:")
    for i in _list:
        print(i)

main()