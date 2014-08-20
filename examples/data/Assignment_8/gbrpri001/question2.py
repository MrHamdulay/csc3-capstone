"""PRIYANKA GOBERDHAN
QUESTION TWO
08/05/14"""

count=0

def string_count(word):
    global count
    if word == '':
        return count
    else:
        if(len(word) > 1 and word[0] == word[1]):
            count = count + 1
            return string_count(word[2:len(word)])

        else:
            return string_count(word[1:len(word)])


x=input("Enter a message:\n")         

print("Number of pairs:", string_count(x))