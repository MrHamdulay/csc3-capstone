def pairs(text):
    if len(text) <= 1:
        return 0
    elif text[0]==text[1]:
        return 1 + pairs(text[2:])
    else:
        return 0 + pairs(text[2:])

message = input("Enter a message:\n")
print('Number of pairs: ', end = '')
print(pairs(message))

