'''porgram to simulate BBS
Simangaliso Mlangeni
MLNSIM014
16 April 2014'''


print("Welcome to uct BBS")
print("MENU")
#Options user can take
print("(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")
#response from user
response = input("Enter your selection:\n")
response = response.upper()#changing response to Capital letters so that it will correspond with control statement conditions

def BBC(response):
    if response=='E':
        Eres = input("Enter the message:\n")
    elif response=='V':
        print("test message")
    elif response=='L':
        print("42.txt, 1015.txt")
    elif response=='D':
        fileName = input("Enter the filename:\n")
        if fileName=='42.txt':
            print("The meaning of life is blah blah blah ...")
        elif filename=='1015.txt':
            print("Computer science class notes ... simplified")
            print("Do all work\nPass courses\nBe happy")
    elif response=='X':
        print("Goodbye!")
#print result from selected option
print(BBC(response))