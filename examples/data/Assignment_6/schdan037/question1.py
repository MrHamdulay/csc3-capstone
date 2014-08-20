"""Daniel Schwartz
SCHDAN037
question 1
april 2014"""


def main():
    """main"""

    strings = []

    # put all strings in list
    string = input("Enter strings (end with DONE):\n")
    # sentinel DONE
    while string != "DONE":
        strings.append(string)
        string = input("")

    # find longest string
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s

    longest = str(len(longest))

    # print formatted strings
    print()
    print("Right-aligned list:")

    for i in range(len(strings)):
        print_str = "{0:>"+longest+"}"
        print_str = print_str.format(strings[i])
        print(print_str)


# runs main on entry
if __name__ == '__main__':
    main()