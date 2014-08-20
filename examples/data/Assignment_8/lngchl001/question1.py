#Program that uses recursion to check for palindromes
#By Chloe Longmore
#5 May 2014

string=input("Enter a string:\n")
      
def palin(string):
    last_pos=len(string)-1
    #base case if the string is empty
    if string=='':
        print("Palindrome!")
    #compares first and last letters to see if the same
    elif string[:1] == string[last_pos:]:
        string=string[1:last_pos]
        #if the same, recurses program
        return palin(string)
    # if not the same, not a palindrome
    elif string[:1] != string[last_pos-1:]:
        print("Not a palindrome!")

palin(string)