import os

def get_assignment_number(name):
    ''' gets the assignment number from a folder name
        @param String name, e.g. Assignment_1
        @return Int 1 '''
    return int(name.split('_')[1])

assignment_folders = []
assignment_numbers = []

os.chdir('data')
for name in os.listdir('.'):
    if os.path.isdir(name):
        assignment_folders.append(name)

for name in assignment_folders:
    number = get_assignment_number(name)
    assignment_numbers.append(number)

print(assignment_numbers)
