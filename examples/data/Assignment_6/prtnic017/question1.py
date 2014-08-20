# Student Number: PRTNIC017
# Date: 4/22/14

names = []

print('Enter strings (end with DONE):')
string = input('')
while string != 'DONE':
    if string not in names:
        names += [string]
    string = input('')

print('\nRight-aligned list:')
if names:
    longest = max(len(name) for name in names)
    form = "%" + str(longest) + "s"
    for name in names:
        print(form % name)