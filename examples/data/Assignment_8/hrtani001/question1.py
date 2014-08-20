#Aniq Hartle
#Check for palindrome
#09/05/2014

'''recursive function that takes in word and reverses it'''
def reverse(word):
    if word == "":    #if the function has reached the end of the input string
        return word
    else:
        return (reverse(word[1:])+word[0])   #compile the reverse of the word

#check if input is same as reverse by calling method and print result
inWord = input("Enter a string:\n")
if inWord == reverse(inWord):
    print("Palindrome!")
else:
    print("Not a palindrome!")