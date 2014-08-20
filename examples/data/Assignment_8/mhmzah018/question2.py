"""Assignment 8 - question 2
Zaheer Mahmood
04 - 05 - 2014"""

sentence = input("Enter a message:\n")

def count(answer):
    pairs = 0
    if len(answer) < 2:
        return pairs 
    else:
        if answer[0] == answer[1]:
            pairs+=1
            return pairs + count(answer[2:])
        else:
            return pairs + count(answer[1:])

print("Number of pairs:",count(sentence))
