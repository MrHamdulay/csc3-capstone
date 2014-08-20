def main(word):
    if word == " ":
        return 0
    else:
        print("Number of pairs:",end=" ")
        return len(word)

sentence = input("Enter a message:\n")
word = sentence.split(" ")

print(main(word))