# anna borysova
# q2, ass8
# 2014 - 05 - 06

i = 0
def pairs(string, i):
    if len(string) == 1 or len(string) == 0:
        return i
    if string[0] == string[1]:
        return pairs(string[2:], i+1)
    return pairs(string[2:], i)

message = input("Enter a message:\n")
print("Number of pairs:", pairs(message, i))