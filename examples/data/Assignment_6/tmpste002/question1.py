""" Right-align a list of strings """
__author__ = 'Stephen Temple'
__date__ = '2014/04/23'


string_array = []

# Populate string array with inputs excluding terminator
string = input("Enter strings (end with DONE):\n")
while string != 'DONE':
    string_array.append(string)
    string = input('')

# Find longest string in array
length = 0
for s in string_array:
    if len(s) > length:
        length = len(s)

# Print formatted output
print("\nRight-aligned list:")
output = "{: >" + str(length) + "}"
for s in string_array:
    print(output.format(s))