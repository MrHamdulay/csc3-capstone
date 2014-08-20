"""counts pairs of letters in a string
Paul Freund
May 2014"""

def pair_counter(count, s):
    """counts pairs of letters in s, returns count"""
    if len(s) <= 1:
        return count
    else:
        if s[0] == s[1]:
            count += 1
            return pair_counter(count, s[2:])
            
        else:
            return pair_counter(count, s[1:])
            
            
        
def main():
    """formats input and output for marker"""
    s = input('Enter a message:\n')
    pairs = pair_counter(0, s)
    print('Number of pairs:', pairs)

if __name__ == '__main__':
    main()