
def encrypted(p):
    if len(p) == 1:
        if p.islower():
            if p == 'z':
                return 'a'
            else:
                return chr(ord(p) + 1)
        else:
            return p
    else:
        return encrypted(p[0]) + encrypted(p[1:])

string = input("Enter a message:\n")
print("Encrypted message:")
print(encrypted(string))
