"""A7Q1 - Unique word counter
27/04/2014
CRNKEE002"""

def main():
    print_words(get_words())

def get_words():
    arrWords = []
    word = input("Enter strings (end with DONE):\n")
    while word.upper() != 'DONE':
        if word not in arrWords:
            arrWords.append(word)
        word = input()
    return arrWords

def print_words(array):
    print() #because automatic marker
    print("Unique list:")
    for i in range(len(array)):
        print(array[i])
            
if __name__ == '__main__':
    main()