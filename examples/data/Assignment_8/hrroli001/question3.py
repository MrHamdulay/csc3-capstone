# Question 3 - Assignment 8
# Oliver Harrison
# 6 May 2014


def secret(msg):
    global new_msg
    if msg == "":
        return
    elif msg[:1] == " ":
        print(" ", end="")
        return secret(msg[1:])
    elif msg[:1].isupper():
        print(msg[:1], end="")
        return secret(msg[1:])
    else:
        if msg[:1] == "z" or msg[:1] == "Z":
            print("a", end="")
            return secret(msg[1:])
        elif msg[:1] == ".":
            print(".", end = "")
        else:
            print(chr(ord(msg[:1])+1), end="")
                  #new_msg += msg[:1]
            return secret(msg[1:])
    


new_msg = ""
msg = input("Enter a message:\n")
print("Encrypted message:")
secret(msg)
