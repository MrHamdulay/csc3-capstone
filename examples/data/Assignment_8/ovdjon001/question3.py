""" Assingment 8, question3.py
by Jonathan Ovadia 
on 4th May 2014"""
def main():
    string = input("Enter a message:\n")
    print("Encrypted message:")
    encrypt(string)

def encrypt(string,encrypted = ""):
    if len(string) == 0:
        print(encrypted)
    else:
        if string[0].isupper() or not string[0].isalpha():
            new_string = encrypted + string[0]
        elif string[0] =="z":
            new_string = encrypted + chr(ord(string[0])-25)
        elif string[0] ==" ":
            new_string = encrypted + " "
        else:
            new_string = encrypted + chr(ord(string[0])+1)
        encrypt(string[1::],new_string)

if __name__ == "__main__": main()
