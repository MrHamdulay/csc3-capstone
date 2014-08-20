def check_pairs(string):
    if len(string) > 1:
        if string[0] == string[1]:
            return 1 + check_pairs(string[2:])
        else:
            return check_pairs(string[1:])
    else:
        return 0
    
string = input('Enter a message:\n')
if string == '':
    print()
pairs = check_pairs(string)
print('Number of pairs:', pairs)