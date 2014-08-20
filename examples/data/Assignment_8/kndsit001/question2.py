"""Program to Count Pairs
Sithasibanzi Kondleka
9 May 2014"""

message = input("Enter a message:\n")

def pairs(string):
    if len(string) == 0:
        return 0 #counter must not add 1
    if len(string) == 1:
        return 0 #counter must not add 1
    if string[0] == string[1]: #checking the consecutive letters
        return 1 + pairs(string[2:]) #adding 1 to counter and checking again
    else:
        return pairs(string[1:])

print("Number of pairs:", pairs(message))