#Program that reverses the word
#Gordon Skhosana
#8/05/2014

def reverse(word):
    if word=="":
        return ""
    else:
        return word[-1] + reverse(word[0:len(word)-1])
def main():
    word=input("Enter a string:\n")
    reverse(word)
    if word==reverse(word):
        print("Palindrome!")
    else:
        print("Not a palindrome!")
main()