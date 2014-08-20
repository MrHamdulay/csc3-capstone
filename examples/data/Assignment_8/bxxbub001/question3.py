def code(s):
    if s == "":
        return s
    elif s[0].islower():
        if s[0] == "z":
            return "a" + code(s[1:])
        elif s[0] == " ":
            return " " + code(s[1:])
        else:
            return chr(ord(s[0])+1) + code(s[1:])
    else:
        return s[0] + code(s[1:])

string1 = input("Enter a message:\n")
print("Encrypted message:")
print(code(string1))