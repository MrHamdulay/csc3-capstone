#question1

def check(word,ii):
    length=len(word)-1
    if ii==length+1:
        return 0
    else:
        if word[ii]==word[length-ii]:
            return word[ii] + str(check(word,ii+1))
        
palindrome=input("Enter a string:\n")

if check(palindrome,0)==palindrome+"0":
    print("Palindrome!")
else:
    print("Not a palindrome!")
