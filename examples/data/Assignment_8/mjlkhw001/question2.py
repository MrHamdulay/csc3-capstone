# Check number of pairs
# Khwezi Majola
# MJLKHW001
# 04 May 2014

def pair(string):
    if len(string) < 2: #Checks if pairs cannot be found
        return 0
    else:
        if string[0] == string[1]: #If the following character is equal
            return 1 + pair(string[2:]) #Recurse excluding the first two characters
        else: return pair(string[1:]) #If not a pair recurse excluding the first character
    
def main():
    string = input('Enter a message:\n')
    print('Number of pairs:', pair(string))

main()