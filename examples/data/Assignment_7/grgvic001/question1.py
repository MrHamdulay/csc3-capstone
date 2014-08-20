#enter values and return all unique values
#victor gueorguiev
#27 April 2014

def main():
    xinput = input('Enter strings (end with DONE):\n')
    strlist = []
    while xinput != 'DONE':
        if not xinput in strlist:
            strlist.append(xinput)
        xinput = input()
    print()
    print('Unique list:')
    for item in strlist:
        print(item)
main()