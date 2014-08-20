""" Program that right aligns a list of strings
 Author: Julius Stopforth (STPJUL004) 
 Date: 2014-04-22 """

#create an empty list
strings = [ ]

#create a sentinel
done = False

#fill the list
print('Enter strings (end with DONE):')
while not done:
    tempstring = input('')
    if tempstring == 'DONE':
        done = True
    else: strings.append(tempstring)

#find the length of the longest string
def find_longest_len(list):
    """ Finds and returns the length of the longest string in the list """
    longest = ''
    for i in list:
        if len(i) > len(longest):
            longest = i
    return len(longest)

maxlen = find_longest_len(strings)

#print the list right aligned to the maximum length
print('\nRight-aligned list:')
for i in strings:
    print('{0: >{1}}'.format(i,maxlen))