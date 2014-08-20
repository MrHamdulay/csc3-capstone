"""check number of pairs of characters in a string
Tim Hardie
9 May 2014"""

def count_pairs (message):
    global num_pairs
    if len (message) > 1:
        if (message[0] == message[1]):
            num_pairs += 1
            count_pairs (message[2:])
        else:
            count_pairs (message[1:])

if __name__ == '__main__':
    message = input ("Enter a message:\n")
    num_pairs = 0
    count_pairs (message)
    print ("Number of pairs:", num_pairs)