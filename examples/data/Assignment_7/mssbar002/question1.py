"""Program to print list of ordered strings without duplicaters"""
def main():
    longList = []
    shortList = []
    inputString = input("Enter strings (end with DONE):\n")
    while inputString != 'DONE':
        longList.append(inputString)
        inputString = input("")
    for item in longList:
        if item not in shortList:
            shortList.append(item)
    print("\nUnique list:")
    for item in shortList:
        print(item)
main()