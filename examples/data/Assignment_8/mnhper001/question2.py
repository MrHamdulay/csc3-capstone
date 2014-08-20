def rep_characters(string):
    if len(string)==1:
        return 0
    if string=="":
        return 0
    else:
        if string[0]!=string[1]:
            return 0+rep_characters(string[1:])
        else:
            return 1+rep_characters(string[2:])
a=input("Enter a message:\n")
print("Number of pairs:",rep_characters(a))