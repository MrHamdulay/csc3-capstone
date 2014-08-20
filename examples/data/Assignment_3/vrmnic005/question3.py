def print_framed_message(message, repeat, thickness):
    length = len(message)
    
    # print top of frame
    for row in range(thickness):
        print("{0}+{1}+{0}".format("|" * row,
                                   "-" * (2 * (thickness - row) + length)))
    
    # print repeated messages
    for row in range(repeat):
        print("{0} {1} {0}".format("|" * thickness, message))
    
    # print bottom of frame
    for row in range(thickness - 1, -1, -1):
        print("{0}+{1}+{0}".format("|" * row,
                                   "-" * (2 * (thickness - row) + length)))

if __name__ == "__main__":
    message = input("Enter the message:\n")
    repeat = int(input("Enter the message repeat count:\n"))
    thickness = int(input("Enter the frame thickness:\n"))
    print_framed_message(message, repeat, thickness)
