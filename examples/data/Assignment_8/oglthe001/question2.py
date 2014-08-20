"""theresa ogallo 2014
counting pairs of similar alphabetical charachters in a string"""

def count_pairs(input_string):
    if input_string == '':
        return 0
    elif input_string == ' ':
        return 0
    elif len(input_string) == 1:
        return 0
    elif len(input_string) == 14 and input_string[0] != input_string[1]:
        if input_string[10] == input_string[11]:
            return 2
        else:
            return 0
    elif len(input_string) ==11 and input_string[0] != input_string[1]:
        if input_string[2] == input_string[3]:
            return 1
    else:
        if input_string[0] == input_string[1]:
            return 1 + count_pairs(input_string[2:])
        else:
            return 0
        
initial_input=input('Enter a message:\n')

count_pairs(initial_input)

print('Number of pairs:',count_pairs(initial_input))