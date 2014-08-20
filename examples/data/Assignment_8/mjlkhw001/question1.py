# Palindrome check using recursion
# Khwezi Majola
# MJLKHW001
# 04 May 2014

def palin(string):
    if len(string) < 1:
        return True #Returns true if single character or less
    else:
        if string[0] == string[-1]: #Checks if first and last characters are equal
            return palin(string[1:-1]) #Recursion occurs with the above checked characters excluded
        else: return False #Returns false if no matching pair found

def main():
    string = input('Enter a string:\n') #Asks for input
    check = palin(string) 
    if check == True: #Prints ouput
        print('Palindrome!')
    else: print('Not a palindrome!')

if __name__ == '__main__':
    main()