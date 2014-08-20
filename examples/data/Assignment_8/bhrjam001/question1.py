# Question 1 Assignment 8
# James Behr
# 2014-05-05

def recursive_reverse(string, index = 0):
    # We need an index as we can't use string slicing
    # Default parameter for first iteration
    
    if index == len(string) - 1:
        return string[index]
    output = recursive_reverse(string, index + 1) + string[index]
    return output

def main():
    print('Enter a string:')
    string = input()
    if recursive_reverse(string) == string:
        print('Palindrome!')
    else:
        print('Not a palindrome!')    

if __name__ == '__main__':
    main()