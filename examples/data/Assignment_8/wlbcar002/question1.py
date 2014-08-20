"""Palindrome checker using recursion
Carla Wilby
4th May 2014"""

string_in = input("Enter a string:\n")
count = 0

def palin_checker(count):
    if (string_in[count] == string_in[len(string_in)-count-1]) and count <= (len(string_in)//2): #if inverted characters are the same, and count is less than halfway
        count += 1
        palin_checker(count)  #keep checking
    elif count == (len(string_in)//2 + 1): #if final value of count is halfway
        print("Palindrome!")
    else:
        print("Not a palindrome!")
    

if __name__ == '__main__':   
    palin_checker(count)