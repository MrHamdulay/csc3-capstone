"""nasha somoina meoli
6th may 2014
program to find pairs of letters in strings"""

def find_pairs(word,s):
    #remove spaces
    word = word.replace(" ","")
    #base case
    if s == "" or len(s) ==1:
        return 0
    #check whether two elements that follow each other are the same
    elif s[0] == s[1]:
        word.replace(s[0],"")
        return 1 + find_pairs(word,s[2:])
    #if none are found run the function again
    else:
        return find_pairs (word,s[1:])
word = input("Enter a message:\n")

s = word 
print("Number of pairs:",str(find_pairs(word,s)))