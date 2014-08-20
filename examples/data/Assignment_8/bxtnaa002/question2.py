# question2.py
# program that uses a recursive function to count the number of pairs of repeated characters in a string
# author: bxtnaa002
# May 2014


msg = input("Enter a message:\n")
def pairs(msg):
    if len (msg) > 1:
        if msg[0] == msg[1]:
            return 1 + pairs(msg[2:])
        else:
            return pairs(msg[1:])
    else:
        return 0

print("Number of pairs:", pairs(msg))


    