def encrypt(s):
    if s == "":
        return ""
    k = ord(s[0]) - ord('a')
    if k < 0 or k >= 26:
        return s[0] + encrypt(s[1:])
    k += 1
    k %= 26
    k = chr(k + ord('a'))
    return k + encrypt(s[1:])

a = input("Enter a message:\n")
print("Encrypted message:")
print(encrypt(a))
