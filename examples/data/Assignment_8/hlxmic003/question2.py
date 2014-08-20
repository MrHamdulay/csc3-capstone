# Michaela Heale
# Assignment 8 Question 2
# counter

def count(word):
    if not len(word)>= 2:
        return 0
    if word[0] == word[1]:
        return 1 + count(word[2:])
    return count(word[1:])
       

def main():
    hat = input("Enter a message:\n")
    tote = count(hat)
    print("Number of pairs:",end=" ")
    print(tote)
        
main()
        