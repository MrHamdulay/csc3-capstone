# I dont understand what this program does
# MSHMUT003
# 28 april 2014

def something():
    # An empty list
    wrd_book = []
    # Prompt the user to input strings
    wrds = input('Enter strings (end with DONE):\n')
    while wrds != 'DONE':
        if wrds not in wrd_book:
            wrd_book.append(wrds)
        elif wrds in wrd_book:
            pass
        wrds = input('')
    print()
    print('Unique list:')
    for i in wrd_book:
        print (i)
something()