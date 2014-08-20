# question2.py
# a program that uses a recursive function to count the number
# of parits of repeated characters in a string
# Thomas Konigkramer
# 5 May 2014

message = input("Enter a message:\n")
counter = 0

def pair_counter(message):
    global counter
    if message == "":
        print("Number of pairs:", counter)
    elif message[:1] == message[1:2]:
        counter += 1
        return pair_counter(message[2:])
    else:
        return pair_counter(message[1:])

pair_counter(message)