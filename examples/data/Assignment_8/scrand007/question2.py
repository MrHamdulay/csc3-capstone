
string = input("Enter a message:\n")

def double(string):
    if len(string) == 0 or len(string) == 1:
        return 0
    elif string[0] != string[1]:
        return double(string[1:])
    elif string[0] == string[1]:
        
        try:
            return 1 + double(string[2:])
        except:
            return 1 + double("")
        
print ("Number of pairs:", double(string))
    