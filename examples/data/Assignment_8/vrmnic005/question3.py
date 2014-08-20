#VRMNIC005
#assignment 8, question 3

def convert_chr(character):
    if character.islower():
        return chr(((ord(character) - 96) % 26) + 97)
    return character
    
def convert_string(string):
    if string == "":
        return ""
    return convert_chr(string[0]) + convert_string(string[1:])

string = input("Enter a message:\n")
print("Encrypted message:", convert_string(string), sep="\n")
