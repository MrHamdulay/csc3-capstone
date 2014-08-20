# Question 2 - Assignment 8
# Oliver Harrison
# 6 May 2014


def rep_char(msg):
    if msg == "":
        return 0
    elif msg[:1] == msg[1:2]:
        return 1 + rep_char(msg[2:])
    else:
        return 0 + rep_char(msg[2:])
        




msg = input("Enter a message:\n")
print("Number of pairs:", rep_char(msg))