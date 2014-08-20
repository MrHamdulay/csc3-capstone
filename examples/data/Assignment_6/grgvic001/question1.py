#program to accept names as strings and then to print right aligned by longest name
#victor gueorguiev
#19 april 2014

def main():
    maxlength = 0
    list_names = []
    x = input('Enter strings (end with DONE):\n')
    while x != 'DONE':      
        list_names.append(x)
        if len(x) > maxlength:
            maxlength = len(x)
        x = input('')
    print('\nRight-aligned list:')
    for name in list_names:
        print(('{0:>'+str(maxlength)+'}').format(name))
main()