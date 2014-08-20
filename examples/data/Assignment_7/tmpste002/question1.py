""" Enter a list of strings and these strings are then printed in the same order but without duplicates """
__author__ = 'Stephen Temple'
__date__ = '2014/04/29'


def main():
    string_array = []
    string = input("Enter strings (end with DONE):\n")
    while not string == 'DONE':
        if not string in string_array:
            string_array.append(string)
        string = input()

    print("\nUnique list:")
    for s in string_array:
        print(s)


if __name__ == '__main__':
    main()