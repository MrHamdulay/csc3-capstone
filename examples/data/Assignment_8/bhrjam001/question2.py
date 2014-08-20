# Question 2 Assignment 8
# James Behr
# 2014-05-05

def count_pairs(string):
    if len(string) < 2:
        return 0
    else:
        if string[0] == string[1]:
            # Slice 2 from beginning to prevent pair overlapping.
            # There is a match, so we can ignore both thus letter and the next.
            return 1 + count_pairs(string[2:])
        else:
            # Ignore this letter, but we still need to test the next one, so 
            # slice 1 from beginning.
            return count_pairs(string[1:])
     
def main():   
    print('Enter a message:')
    message = input()
    print('Number of pairs:', count_pairs(message))

if __name__ == '__main__':
    main()