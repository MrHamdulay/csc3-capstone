"""Program that uses a recursive function to count the number of pairs of repeated characters in a string
Telisha Ramlall
4 May 2014"""


def count_doubles(string, i):
    #returnnumber of doubles when of string is 1 after being evaluated
    if len(string) == 1 or len(string) == 0:
        return i
    #remove two letters from the whole string if consecutive letters are equal
    elif string[0] == string[1]:
        i += 1
        return count_doubles(string[2:], i)
    #If not equal, remove the first letter so it can be compared to the next.
    else:
        return count_doubles(string[1:], i)

i = 0
string=input('Enter a message:\n')
print('Number of pairs:',count_doubles(string, i))