# Miengha Behardien
# Assignment 8
# 4 May 2014

def pairs(string):          #counts number of letter pairs in a string
    count=0
    if len(string)<=1:
        return count
    elif string[0]==string[1]:
        count+=1
        return pairs(string[2::]) + count       #adds to count if letters next to eachother are the same
    else:
        return pairs(string[2::]) + count

def main():
    string=input("Enter a message:\n")      #deals with all the extra stuff to make it look pretty
    string=pairs(string)
    print("Number of pairs:", string)

main()