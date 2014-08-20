"""A8Q2 - Character Pairs
5/3/2012
CRNKEE002"""

def main():
    message = input('Enter a message:\n')
    print('Number of pairs:', double_chars(0, message))

def double_chars(pos, word):
    if len(word) == 1 or len(word) == 0:
        return 0
    elif (word[pos] == word[pos+1]) and (pos+1 == len(word)-1):
        return 1
    elif (word[pos] == word[pos+1]) and (pos+1 < len(word)-1):
        return 1 + double_chars(0, word[2::])
    elif (word[pos] != word[pos+1]) and (pos+1 == len(word)-1):
        return 0
    elif (word[pos] != word[pos+1]) and (pos+1 < len(word)-1):
        return double_chars(0, word[1::])
            
if __name__ == '__main__':
    main()