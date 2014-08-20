'''Adam Rosendorff RSNADA001
03 May 2014
CSC1015F Assignment 8 Q2'''
def char_pairs(text):
    if text == '' or len(text) == 1:
        return 0
    if text[0] == text[1]:
        return 1 + char_pairs(text[2:])
    else: 
        return 0 + char_pairs(text[2:])
userin = input('Enter a message:\n')
print('Number of pairs:',char_pairs(userin))
