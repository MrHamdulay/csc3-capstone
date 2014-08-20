count=0

def pairs(phrase):
    global count
    if len(phrase)<=1:
        print(count)
    elif phrase[0]==phrase[1]:
        count = count+1
        return pairs(phrase[2:])
    else:
        return pairs(phrase[2:])

phrase = input("Enter a message:\n")
print("Number of pairs: ",end ="")
pairs(phrase)