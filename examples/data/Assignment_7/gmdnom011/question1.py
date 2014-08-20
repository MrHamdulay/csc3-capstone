# Program to remove duplicates in a list of strings
# Nomsa Gamedze
# 28 April 2014

def main():
    print("Enter strings (end with DONE):")
    string = input("")
    strings = ""
    while string != "DONE":
        strings += string + "sep"
        string = input("")
    strings = strings.split("sep")
    print('\n'"Unique list:")
    done = []
    for i in strings:
        if i in done:
            continue
        else:
            done.append(i)
            print(i)


main()