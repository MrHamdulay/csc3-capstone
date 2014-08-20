"""CSC1015F Assignment 8 Question 2
Xola Matlanyane MTLXOL002
9 May 2014"""

def counting(text, c, n):
    if len(text) <= c:        #if the end of the text is reached, return number of pairs
        return n
    if text[c-1] == text[c]:  #if the two consecutive characters are the same
        n += 1                  #then we increase the counter for pairs found
        c += 2
    else:
        c += 1                      #check the next se of characters
    return counting(text, c, n)

x = input("Enter a message:\n")
y = counting(x, 1, 0)
print("Number of pairs:", y)