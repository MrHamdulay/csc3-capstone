#MKXTAT001 Tato Moaki
#Assignment8 question2
#Program counts number of equal pairs in a string

def main():
    user_input = input("Enter a message:\n")
    print("Number of pairs:",count_chr(user_input))    

def count_chr(string):
    """function returns a count of equal pairs in a string"""
    if len(string) <= 1:
        return 0         
    else:
        if string[0] == string[1]:
            return 1 + count_chr(string[2:])
        else:
            return count_chr(string[1:])
            
if __name__=="__main__":
    main()
        