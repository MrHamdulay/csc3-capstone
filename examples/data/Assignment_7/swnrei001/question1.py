"""Assignment 7, Question 1
Take a list of strings, ending with sentinel DONE.
Print the strings in the same order, but without duplicates
author: SWNREI001
28 April 2014"""

def main():
    """Main module of program; does what is explained above"""
    lines = []
    s = input("Enter strings (end with DONE):\n")
    while s != "DONE":
        if s in lines:
            pass  # skip if it is a duplicate
        else:
            lines.append(s)
        s = input()
    print("\nUnique list:")
    for i in lines:
        print(i)

if __name__ == "__main__":
    main()