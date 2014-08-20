"""Daniel Schwartz
SCHDAN037
question 1
April 2014"""

def main():
    """main"""
    strings = []
    string = input("Enter strings (end with DONE):\n")
    while string != "DONE":
        if string not in strings:
            strings.append(string)
        string = input("")

    print()
    print("Unique list:")
    for s in strings:
        print(s)


if __name__ == '__main__':
    main()