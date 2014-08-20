


def rev(text,revtext, c):
    c += 1
    if len(text) < c:
        return True
    if len(revtext) == len(text):
        return True
    else:
        revtext += text[len(text)-c]
    if revtext[len(revtext)-1] == text[c-1]:
        return rev(text,revtext,c)
    else:
        return False


def main():
    x=input("Enter a string:\n")
    y=rev(x,"",0)
    if y == True:
        print("Palindrome!")
    else:
        print("Not a palindrome!")

main()