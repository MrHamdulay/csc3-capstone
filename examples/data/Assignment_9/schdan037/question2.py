"""Daniel schwartz
SCHDAN037
question 2
may 2014"""


def main():
    """main"""
    # ask for info
    in_filename = input("Enter the input filename:\n")
    out_filename = input("Enter the output filename:\n")
    width = int(input("Enter the line width:\n"))

    # retrieve file contents
    in_file = open(in_filename, "r")
    lines = in_file.readlines()
    in_file.close()

    # manipulate file contents
    #   FIX THE PARAGRAPHS
    print(lines)
    oneline = ""
    for line in lines:
        if line == "\n":
            oneline += "\n\n"
        else:
            oneline += line.strip("\n")
    final_string = ""
    count = 0
    for word in oneline.split(" "):
        if count + len(word) > width:
            final_string += "\n" + word + " "
            count = len(word) + 1
        else:
            final_string += word + " "
            count += len(word) + 1

    #print(final_string)
    # write to new file
    out_file = open(out_filename, "w")
    print(final_string, file=out_file)
    out_file.close()

#run main on entry
if __name__ == "__main__":
    main()