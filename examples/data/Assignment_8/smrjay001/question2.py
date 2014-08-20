"""
Assignment 8 - Question 2
A program to count the number of pairs of characters in a string.
Jayan Smart
6 May 2014
"""

def find_pairs (string, count):
    if len(string) < 2:
        print("Number of pairs:", count)
        return count
    if string[0] == string[1]:
        count+=1
        return find_pairs(string[2:], count)
    else:
        find_pairs(string[1:], count)

def main():
    text = input("Enter a message:\n")
    find_pairs(text, 0)
    
    
if __name__ == "__main__":
    main()
