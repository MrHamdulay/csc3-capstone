# Program to reformat text files
# Nomsa Gamedze
# 11 May 2014

def format_file(file, width):
    text = file.read()
    text_in = text.replace("\n\n", "(newline)")
    text_in = text_in.replace("\n", " ")
    text_in = text_in.replace("(newline)", "\n\n")
    x = len(text_in)
    y = x//width
    text_out = []
    for c in range(y+1):
        text_out.append("")
    items = text_in.split(" ")
    c = 0
    for i in range(len(text_out)):
        while len(text_out[i]) + len(items[c]) <= width:
            text_out[i] += items[c] + ' '
            if c < (len(items)-1):
                c += 1
            else:
                break
    text_out[i] = text_out[i][:len(text_out[i])-1]
    return text_out

def main():
    filename_in = input("Enter the input filename:"'\n')
    file = open(filename_in, 'r')
    filename_out = input("Enter the output filename:"'\n')
    width = eval(input("Enter the line width:"'\n'))
    formatted = format_file(file, width)
    string = '\n'.join(formatted)
    print(string, file = open(filename_out, 'w'))

main()