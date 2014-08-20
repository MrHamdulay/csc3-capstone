pairs = 0


def no_pairs(inpt):
    if len(inpt) <= 1:
        return ""
    elif inpt[0] == inpt[1]:
        global pairs
        pairs += 1
        no_pairs(inpt[2:])
    else:
        no_pairs(inpt[1:])


str_inpt = input("Enter a message:\n")
no_pairs(str_inpt)
print("Number of pairs:", pairs)