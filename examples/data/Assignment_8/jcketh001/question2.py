#Program to count number of pairs of repeated strings
#Ethan Jackson
#9 May 2014

n = input("Enter a message:\n")
def num_pairs (n):
    if len(n) == 1:#if one character, then there are no pairs
        return 0
    if len(n) == 2 and n[0] == n[1]:#if there are two characters, and if they are the same, then 1 pair
        return 1
    if n[0] == n[1]:#if the first two letters are equal, then run through the function again
        return 1 + num_pairs(n[2:])
    else:
        return num_pairs(n[1:])
print("Number of pairs:", num_pairs(n))
