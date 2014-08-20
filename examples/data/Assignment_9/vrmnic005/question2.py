import textwrap

input_file_name = input("Enter the input filename:\n")
output_file_name = input("Enter the output filename:\n")
width = int(input("Enter the line width:\n"))

with open(input_file_name, "r") as input_file:
    paragraphs = input_file.read().split("\n\n")

with open(output_file_name, "w") as output_file:
    for paragraph in paragraphs:
        print(textwrap.fill(paragraph, width), end="\n\n", file=output_file)