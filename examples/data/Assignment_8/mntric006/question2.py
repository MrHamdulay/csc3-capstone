def countpairs (word):
    if not (len(word) >= 2): return 0
    if word[0] == word[1]: return 1 + countpairs(word[2:])
    return countpairs(word[1:])


wordin = input("Enter a message:\n")
print("Number of pairs: " + str(countpairs (wordin)))

