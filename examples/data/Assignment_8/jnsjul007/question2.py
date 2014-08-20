# Julian van Rensburg
# Assignment 8 Question 2
# counter

def count(word):
    if not len(word)>= 2:
        return 0
    if word[0] == word[1]:
        return 1 + count(word[2:])
    return count(word[1:])
       

def main():
    a = input("Enter a message:\n")
    b = count(a)
    print("Number of pairs:",end=" ")
    print(b)
        
main()
        