def encrypt(word,num):
    if not num == (len(word)):
        if not word[num] == " ":
            eletter = chr(ord(word[num])+1)
            num+=1
            print(eletter,end="")
            encrypt(word,num)
        elif word[num] == " ":
            print(" ",end="")
            num+=1
            encrypt(word,num)

wordin = input("Enter a message:\n")
count = 0
print("Encrypted message:")
encrypt(wordin,count)
