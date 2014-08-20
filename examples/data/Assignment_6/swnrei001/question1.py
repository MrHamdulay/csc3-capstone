"""Assignment 6, Question 1
Right-align a list of strings
SWNREI001
20/4/2014"""

def list_max(strings):
    """Takes a list of strings and returns the length of the longest string"""
    max_len = 0
    for i in strings:
        if len(i) > max_len:
            max_len = len(i)
    return max_len

def ralign(string_list):
    """Takes a list of strings and prints them right-aligned"""
    length = list_max(string_list)
    print("Right-aligned list:")
    for i in string_list:
        print(("{0:>" + str(length) + "}").format(i))

def main():
    """Main function of module; gets a list of strings ending with 'DONE'
    Prints the list right-aligned"""
    s = input("Enter strings (end with DONE):\n")
    strings = []
    while s != "DONE":
        strings.append(s)
        s = input()
    print()
    ralign(strings)

if __name__ == "__main__":
    main()