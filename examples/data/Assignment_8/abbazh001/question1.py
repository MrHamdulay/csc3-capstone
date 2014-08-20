#Azhar Aboobaker
#ABBAZH001
#07/05/2014


def reversestring(string):
    if string == "" or len(string) == 1 :
        print("Palindrome!")
    else:
        if string[0] == string[-1] :
            return reversestring(string[1:-1])
        else:
            print("Not a palindrome!")
    
string = input("Enter a string:\n")

reversestring(string)

    