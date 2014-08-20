"""A programme to count the number of reapeted characters on a string
Tsanwani Vhonani
06 May 2014"""

#get message from usser
msg=input("Enter a message:\n")
def no_repeated(msg):
    if len(msg)<2:
        return 0
    if msg[0]==msg[1]:
        return 1+ no_repeated(msg[2:])
    else:
        return no_repeated(msg[1:])
print("Number of pairs:",no_repeated(msg))
