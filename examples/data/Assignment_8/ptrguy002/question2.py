def count(x, s):
    if x >= len(s)-1:
        return 0
    inp = 0
    if s[x] == s[x+1]:
        inp = 1
        x += 1
    return inp + count(x+1, s)

a = input("Enter a message:\n")
print("Number of pairs: " + str(count(0, a)))
