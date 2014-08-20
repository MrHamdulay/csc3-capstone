""" Reformat a text file so that all lines are at most a given length. Do not break up words.
Write the formatted text to a new text file """
__author__ = 'Stephen Temple'
__date__ = '2014/05/12'


def main():
    # Open file
    input_file_name = input("Enter the input filename:\n")
    with open(input_file_name, 'r') as input_file:
        input_lines = input_file.readlines()

    output_file_name = input("Enter the output filename:\n")

    # Convert to single array of words
    words = []
    for line in input_lines:
        if line != '\n' and line[-1] == '\n':
            line = line[:-1]
        words.extend(line.split(' '))

    line_width = eval(input("Enter the line width:\n"))
    current_line_width = 0
    text = ''
    for word in words:
        length = len(word)
        if word == '\n':  # if word is new line add new line only
            text += '\n\n'
            current_line_width = 0
        elif current_line_width == 0:  # if start of line
            text += word  # add word only
            current_line_width += length
        elif current_line_width + length + 1 <= line_width:  # if in middle of line and enough width remaining
            text += ' ' + word  # add space followed by word
            current_line_width += length + 1
        else:  # if not enough width remaining
            text += '\n' + word  # add new line followed by word
            current_line_width = length

    with open(output_file_name, 'w') as output_file:
        output_file.write(text)


if __name__ == '__main__':
    main()