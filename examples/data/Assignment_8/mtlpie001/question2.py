#MOTALAOTA PIET
#11 MAY 2014
def question2(word):
    x=0
    if len(word) < 2 :
        return 0
    elif word[0]==word[1]:
        return  question2(word[2:]) + 1
    else:
        return question2(word[2:]) + 0

if __name__=='__main__':
    word = input("Enter a message:\n")
    print("Number of pairs:",question2(word))
