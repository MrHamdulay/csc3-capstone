#maisha Ivha 
#a programme that count the number of pairs of repeated characters in a string
#09 may 2014

#def main():
word=input("Enter a message:\n")
def numb_pairs(word):
    #base case, the recursive should not continue under this condition
    
    if word==""or len(word)==0:

        return 0

    else: #the begining of the recursive step

        if word[0:1]==word[1:2]: #a programe starts counting the number of pairs from the first two characters of the word

            return 1 + numb_pairs(word[2:]) #the step to add number of pairs fond to the sum of available pairs from the word

        else:

            return numb_pairs(word[1:])

print("Number of pairs:",numb_pairs(word)) #printg the number of pairs available

if __name__ == "__numb_pairs__":
    numb_pairs(word)