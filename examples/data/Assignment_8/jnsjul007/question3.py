# Julian van Rensburg
# Assignment 8 Question 3
# Encryption

def encrypt(word,p):
    if not p == (len(word)):
        if not word[p].isupper():
            if word[p].isalpha():
                if not word[p] == " " and not word[p] == 'z':
                    eletter = chr(ord(word[p])+1)
                    p+=1
                    print(eletter,end="")
                    encrypt(word,p)       
                elif word[p] == " ":
                    print(" ",end="")
                    p+=1
                    encrypt(word,p)
                elif word[p] == 'z':
                    print("a",end="")
                    p+=1
                    encrypt(word,p)
            else:
                print(word[p],end="")
                p+=1
                encrypt(word,p)
        else:
            print(word)
      
def main():
    get = input("Enter a message:\n")
    g = 0
    print("Encrypted message:")
    encrypt(get,g)
        
main()
