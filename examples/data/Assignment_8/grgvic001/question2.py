#count number of double characters with recursion
#victor gueorguiev
#03 May 2014

def count_double_char(n):
    if len(n) <= 1:
        return 0
    if n[0] == n[1]:
        return 1 + count_double_char(n[2:])
    else:
        return count_double_char(n[1:])
    
def main():
    x = input('Enter a message:\n')
    print('Number of pairs:',str(count_double_char(x)))
    
main()
    