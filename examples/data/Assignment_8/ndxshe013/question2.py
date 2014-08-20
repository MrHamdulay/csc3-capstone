

x = input("Enter a message:\n")

def RepeatCharacters (n):
    if len(n)<2:
        return 0
    elif n[0]== n[1]:
        return 1+RepeatCharacters(n[2:])
    else:
        return RepeatCharacters(n[1:])
print("Number of pairs:",RepeatCharacters(x))

