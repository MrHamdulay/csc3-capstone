#Siphesihle Cele
#10 May 2014
#Assignment 8
#rercursive function that counds repeats in a sentence
#FIRST, PYTHON READS THE SENTENCE
#going through all the elements it counts the pair of letters that are repeated
#prints number of pairs that are repeated.

c = 0
def count_pairs(state):
    if len(state)<=1:
        return c
    else:
        if state[0] == state[1]:
            global c
            c += 1
            return number_pairs(state[2::])
        else:
            return number_pairs(state[1::])
def main():
    c = 0
    user_input = input("Enter a message:\n")
    print("Number of pairs:",number_pairs(user_input))
main()
        