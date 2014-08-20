#Amitha Doodnath - DDNAMI001
#08/05/2014
#Programme to find palindromic strings

def reverse(word):
    if word=="":
        return word
    else:
        return word[len(word)-1:] + reverse(word[:len(word)-1])
    
def main():
    word=input("Enter a string:\n")
    
    if word==reverse(word):
        print("Palindrome!")
    else:
        print("Not a palindrome!")

main()