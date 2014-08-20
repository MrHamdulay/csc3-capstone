__author__ = 'George de Kock'
"""Program with a recursive function to calculate whether or not a string is a palindrome (reads the sa me if reversed).
2014-05-05"""


def testpalin(text):
    if len(text) <= 1:
        return True
    else:
        if text[0] == text[-1]:
            return testpalin(text[1:-1])

if __name__ == "__main__":
    word = input("Enter a string:\n")
    if testpalin(word):
        print("Palindrome!")
    else:
        print("Not a palindrome!")